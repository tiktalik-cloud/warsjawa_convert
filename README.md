Welcome
-------

This demo show how to use [Tiktalik CPU-hog instances](https://tiktalik.com/en/pricing#unit/cpuhog) to convert video files from one format to another.

Files to convert as well as converted ones are stored on [Tiktalik Files](https://tiktalik.com/en/files) -- an Amazon S3 compatibile storage service.

Setup
-----

1. [Get free Tiktalik.com account](https://tiktalik.com/en/promo?auto=1)

2. Activate [Tiktalik Files](https://tiktalik.com/en/files) service and write down your authorization data -- your login and key.

3. Adjust ```config.py``` file accordingly

4. Read [How to use Vagrant with Tiktalik.com](http://articles.tiktalik.com/content/vagrant/vagrant-beginners/) guide or if you already know it get your API keys from [Tiktalik.com admin panel](https://tiktalik.com/panel/#apikeys).

5. Adjust ```playbook.yml``` file accordingly and put API key and secret where needed.
   Please note that you have to put API keys in two diffrent places in this file.

Usage
-----

1. Upload videos to Tiktalik files:

   ```
   $ ./push.py ./movies/*
   ```

2. Fire up convert task with:

   ```
   $ ansible-playbook -i hosts -vvvv playbook.yml
   ```
   
3. Be patient and wait for ansible to finish its work :-)

4. Browse your converted movies at:

   [https://tiktalik.com/en/panel/#buckets](https://tiktalik.com/en/panel/#buckets)
