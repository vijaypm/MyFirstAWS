__author__ = 'vijay'
import boto
boto.set_stream_logger("boto")
s3 = boto.connect_s3()
rs = s3.get_all_buckets()
print 'S3 buckets'
for b in rs:
    print b
print 'S3 regions'

import boto.s3
regions = boto.s3.regions()
for r in regions:
    print r

#ec2_conn = regions[0].connect()
s3_conn = boto.s3.connect_to_region('us-west-1', debug=2)

print 'EC2 regions'
import boto.ec2
regions = boto.ec2.regions()
for r in regions:
    print r

#ec2_conn = regions[0].connect()
ec2_conn = boto.ec2.connect_to_region('us-west-1', debug=2)
print

