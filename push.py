#!/usr/bin/env python

from boto.s3.connection import S3Connection
from boto.s3.key import Key
from boto.s3.prefix import Prefix
from boto.exception import S3ResponseError, S3CreateError

import sys, os
from config import ACCESS_KEY, ACCESS_SECRET, BUCKET_NAME

s3 = S3Connection(ACCESS_KEY, ACCESS_SECRET, host='sds.tiktalik.com', is_secure=False)

try:
	bucket = s3.create_bucket(BUCKET_NAME)
except S3CreateError:
	pass
bucket = s3.get_bucket(BUCKET_NAME)

# czyscimy bucketa
def rm_prefix(prefix=None):
  keys = bucket.get_all_keys(max_keys=100, prefix=prefix)
  for key in keys:
    if isinstance(key, Prefix):
      rm_prefix(key.name)
    else:
      print "Usuwam plik", key.key
      bucket.delete_key(key)
      
rm_prefix()

files = sys.argv[1:]
for file in files:
  k = Key(bucket)
  k.key = "/uploaded/%s" % os.path.basename(file)
  print "Dodaje plik", file
  k.set_contents_from_filename(file, policy="public-read", headers={"Content-Type": "video/x-msvideo"})
