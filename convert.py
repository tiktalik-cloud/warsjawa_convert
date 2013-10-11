#!/usr/bin/env python

from boto.s3.connection import S3Connection
from boto.s3.key import Key

import shlex, subprocess
import os

from config import ACCESS_KEY, ACCESS_SECRET, BUCKET_NAME

s3 = S3Connection(ACCESS_KEY, ACCESS_SECRET, host='sds.tiktalik.com', is_secure=False)
bucket = s3.get_bucket(BUCKET_NAME)

while True:
  keys = bucket.get_all_keys(max_keys=1, prefix="uploaded/")
  print keys
  if len(keys) == 0:
    break
  key = keys[0]

  key.get_contents_to_filename("/tmp/video_to_convert.avi")
  try:
    os.unlink("/tmp/video_converted.webm")
  except OSError:
    pass

  cmdline = ["ffmpeg", "-i", "/tmp/video_to_convert.avi", "-threads", "8", "-acodec", "libvorbis", "-ac", "2", "-ab", "96k", "-ar", "44100", "-b", "345k", "-s", "640x360", "/tmp/video_converted.webm"]
  ffmpeg = subprocess.Popen(cmdline, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
  stdout, stderr = ffmpeg.communicate()
  print stdout, stderr
  
  original_filename = key.key[9:] # uploaded/
  new_key_location = "converted/" + original_filename[:original_filename.rfind(".")] + ".webm"
  print new_key_location
  
  bucket.delete_key(key)
  
  key = Key(bucket)
  key.key = new_key_location
  key.set_contents_from_filename("/tmp/video_converted.webm", policy="public-read", headers={"Content-Type": "video/webm"})
