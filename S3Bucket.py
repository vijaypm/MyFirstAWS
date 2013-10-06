# Modified code from the book 'Python and AWS Cookbook' by Mitch Garnaat
import boto

def create_bucket(bucket_name):
    """
    Create a bucket.  If the bucket already exists and you have
    access to it, no error will be returned by AWS.
    Note that bucket names are global to S3
    so you need to choose a unique name.
    """
    s3 = boto.connect_s3()

    # First let's see if we already have a bucket of this name.
    # The lookup method will return a Bucket object if the
    # bucket exists and we have access to it or None.
    bucket = s3.lookup(bucket_name)
    if bucket:
        print 'Bucket (%s) already exists' % bucket_name
    else:
        # Let's try to create the bucket.  This will fail if
        # the bucket has already been created by someone else.
        try:
            bucket = s3.create_bucket(bucket_name)
        except s3.provider.storage_create_error, e:
            print 'Bucket (%s) is owned by another user' % bucket_name
    return bucket

def delete_bucket(bucket_name):
    """
    Create a bucket.  If the bucket already exists and you have
    access to it, no error will be returned by AWS.
    Note that bucket names are global to S3
    so you need to choose a unique name.
    """
    s3 = boto.connect_s3()

    # First let's see if we already have a bucket of this name.
    # The lookup method will return a Bucket object if the
    # bucket exists and we have access to it or None.
    bucket = s3.lookup(bucket_name)
    if bucket:
        print 'Deleting bucket with name %s' % bucket.name
        delete_bucket_keys(bucket)
        bucket.delete()
    else:
        print 'Bucket %s not found' % bucket_name
    return bucket

def delete_bucket_keys(bucket):
    #for key in bucket.list():
    #    key.delete()
    bucketListResultSet = bucket.list()
    bucket.delete_keys([key.name for key in bucketListResultSet])


def delete_all_buckets():
    s3 = boto.connect_s3()
    rs = s3.get_all_buckets()
    for b in rs:
        print 'Deleting bucket with name %s' % b.name
        delete_bucket_keys(b)
        b.delete()
    return