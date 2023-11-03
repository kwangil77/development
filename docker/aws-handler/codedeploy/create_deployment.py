#!/usr/bin/env python

from __future__ import print_function
from time import sleep
import argparse
import boto3
from botocore.exceptions import ClientError

parser = argparse.ArgumentParser(
    description='Configures deployment so that you can update to AWS CodeDeploy')
parser.add_argument('--application-name', action='store',
    help='The application name of the deployment for create to AWS CodeDeploy')
parser.add_argument('--group-name', action='store',
    help='The group name of the deployment for create to AWS CodeDeploy')
parser.add_argument('--config-name', action='store',
    help='The config name of the deployment for create to AWS CodeDeploy')
parser.add_argument('--s3-bucket', action='store',
    help='The s3 bucket of the deployment for create to AWS CodeDeploy')
parser.add_argument('--s3-key', action='store',
    help='The s3 key of the deployment for create to AWS CodeDeploy')
parser.add_argument('--bundle-type', action='store',
    help='The bundle type of the deployment for create to AWS CodeDeploy')
args = parser.parse_args()

def get_client():
    """
    Get client for AWS CodeDeploy
    """
    try:
        return boto3.client('codedeploy')
    except ClientError as err:
        print("Failed to create boto3 client.\n" + str(err))
        raise

def create_deployment(client):
    """
    Create deployment to AWS CodeDeploy
    """
    try:
        response = client.create_deployment(
            applicationName=args.application_name,
            deploymentGroupName=args.group_name,
            deploymentConfigName=args.config_name,
            revision={
                'revisionType': 'S3',
                's3Location': {
                    'bucket': args.s3_bucket,
                    'key': args.s3_key,
                    'bundleType': args.bundle_type
                }
            },
            fileExistsBehavior='OVERWRITE'
        )
    except ClientError as err:
        print("Failed to create deployment.\n" + str(err))
        raise

    return str(response['deploymentId'])

def get_deployment(client, deployment_id):
    """
    Get deployment in AWS CodeDeploy
    """
    try:
        response = client.get_deployment(
            deploymentId=deployment_id
        )
    except ClientError as err:
        print("Failed to get deployment.\n" + str(err))
        raise

    deployment_info = response['deploymentInfo']
    
    if str(deployment_info['status']) == 'Succeeded':
        print(str(deployment_info['completeTime']) + ' [' + str(deployment_info['status']) + '] Deployment "' + str(deployment_info["deploymentId"]) + '" is completed.')
        return True
    elif str(deployment_info['status']) in ['Failed', 'Stopped']:
        raise Exception("Failed to get deployment.\n" + str(deployment_info['errorInformation']['message']))
    else:
        return False

def main():
    client = get_client()
    deployment_id = create_deployment(client)

    while not get_deployment(client, deployment_id):
        sleep(15)

if __name__ == "__main__":
    main()