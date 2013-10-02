__author__ = 'vijay'
import os
import boto

EC2_REGION='us-west-1'
AMI_BITNAMI_DJANGOSTACK_UBUNTU32 = 'ami-cee8dd8b'
EC2_USER_BITNAMI='bitnami'
MICRO_INSTANCE = 't1.micro'
INSTANCE_TAG='my-us-west-1'
KEY_NAME='my-us-west-1'
KEY_EXTENSION='.pem'
KEY_DIR='~/.ssh'

KEY_PATH = os.path.join(os.path.expanduser(KEY_DIR),
                                KEY_NAME+KEY_EXTENSION)

boto.set_stream_logger("boto")