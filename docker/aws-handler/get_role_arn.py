#!/usr/bin/env python

from __future__ import print_function
import os
import argparse
import requests

parser = argparse.ArgumentParser(
    description='Configures iam so that you can create to AWS Resource')
parser.add_argument('--tag-part', action='store',
    help='Tag part of role for retrieve to AWS IAM')
args = parser.parse_args()

def get_role_arn():
    """
    Get role arn to AWS Resource
    """
    response = requests.get(
        '{cmdb_api_url}/api/v1/iam/roles'.format(cmdb_api_url=os.environ.get('CMDB_API_URL')), 
        params={
            'awsAccount': os.environ.get('AWS_PROFILE'),
            'classifier': 'team',
            'part': 'ce' if args.tag_part == 'tc' else args.tag_part,
            'scheme': 'ec2',
            'sort': 'id,asc',
            'size': 1
        }).json()

    return response['data'][0]['arn']

def main():
    open('/tmp/role_arn', 'w').write(get_role_arn())

if __name__ == "__main__":
    main()