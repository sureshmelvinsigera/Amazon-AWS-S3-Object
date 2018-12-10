import boto3
from botocore.client import ClientError


def s3_client():
    s3 = boto3.client('s3')
    """ :type : pyboto3.s3 """
    return s3


def create_bucket(name):
    try:
        return s3_client().create_bucket(Bucket=name, CreateBucketConfiguration={
            'LocationConstraint': 'us-west-1'})
    except ClientError:
        print("The bucket does not exist or you have no access.")


if __name__ == '__main__':
    create_bucket("gmp232321")
