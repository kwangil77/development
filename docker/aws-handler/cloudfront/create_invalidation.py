#!/usr/bin/env python

from __future__ import print_function
from datetime import datetime
from time import sleep
import argparse
import boto3
from botocore.exceptions import ClientError

parser = argparse.ArgumentParser(
    description='Configures invalidation so that you can update to AWS CloudFront')
parser.add_argument('--distribution-id', action='store',
    help='The distribution id of the invalidation for create to AWS CloudFront')
args = parser.parse_args()

def get_client():
    """
    Get client for AWS CloudFront
    """
    try:
        return boto3.client('cloudfront')
    except ClientError as err:
        print("Failed to create boto3 client.\n" + str(err))
        raise

def create_invalidation(client):
    """
    Create invalidation to AWS Cloud Front
    """
    try:
        response = client.create_invalidation(
            DistributionId=args.distribution_id,
            InvalidationBatch={
                'Paths': {
                    'Quantity': 1,
                    'Items': [
                        '/*',
                    ]
                },
                'CallerReference': datetime.now().strftime("%Y%m%d%H%M%S")
            }
        )
    except ClientError as err:
        print("Failed to create invalidation.\n" + str(err))
        raise

    return str(response['Invalidation']['Id'])

def get_invalidation(client, invalidation_id):
    """
    Get invalidation in AWS CloudFront
    """
    try:
        response = client.get_invalidation(
            DistributionId=args.distribution_id,
            Id=invalidation_id
        )
    except ClientError as err:
        print("Failed to get invalidation.\n" + str(err))
        raise

    invalidation = response['Invalidation']

    if str(invalidation['Status']) == 'Completed':
        print(str(invalidation['CreateTime']) + ' [' + str(invalidation['Status']) + '] Invalidation "' + str(invalidation["Id"]) + '" is completed.')
        return True
    else:
        return False
    

def main():
    client = get_client()
    invalidation_id = create_invalidation(client)

    while not get_invalidation(client, invalidation_id):
        sleep(20)

if __name__ == "__main__":
    main()