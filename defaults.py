__author__ = 'vijay'
import os
import boto

EC2_REGION='us-east-1'
#EC2_REGION='us-west-1'
AMI_BITNAMI_DJANGOSTACK_UBUNTU32 = 'ami-1dd99174' # us-east-1 region
#AMI_BITNAMI_DJANGOSTACK_UBUNTU32 = 'ami-cee8dd8b' # us-west-1 region
EC2_USER_BITNAMI='bitnami'
MICRO_INSTANCE = 't1.micro'
INSTANCE_TAG=EC2_REGION

KEY_NAME=EC2_REGION
KEY_EXTENSION='.pem'
KEY_DIR='~/.ssh'
KEY_PATH = os.path.join(os.path.expanduser(KEY_DIR),
                                KEY_NAME+KEY_EXTENSION)

#S3_PHOTO_BUCKET='com.mariadassou.myphotosite'
S3_PHOTO_BUCKET='myphotosite'

DJANGO_PORT=8000

#boto.set_stream_logger("boto")