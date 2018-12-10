import boto3
from botocore.client import ClientError
import json


def s3_client():
    s3 = boto3.client('s3')
    """ :type : pyboto3.s3 """
    return s3


def create_bucket(name):
    try:
        s3_client().create_bucket(Bucket=name, CreateBucketConfiguration={'LocationConstraint': 'us-west-1'})
        create_bucket_policy(name)
    except ClientError:
        print("The bucket does not exist or you have no access.")


def create_bucket_policy(name):
    bucket_policy = {
        'Version': '2012-10-17',
        'Statement': [{
            'Sid': 'AddPerm',
            'Effect': 'Allow',
            'Principal': '*',  # allow to public
            'Action': ['s3:*'],  # allow all the operations
            'Resource': ["arn:aws:s3:::%s/*" % name]
        }]
    }

    policy_string = json.dumps(bucket_policy)


if __name__ == '__main__':
    create_bucket("gmp23232111")
