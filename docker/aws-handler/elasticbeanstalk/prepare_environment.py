#!/usr/bin/env python

from __future__ import print_function
from datetime import date, datetime
import os
import sys
import json
import argparse
import boto3
from botocore.exceptions import ClientError

parser = argparse.ArgumentParser(
    description='Configures environment so that you can create to AWS ElasticBeanstalk')
parser.add_argument('--application-name', action='store',
    help='The name of the application for create to AWS ElasticBeanstalk')
parser.add_argument('--environment-name', action='store',
    help='The name of the environment for create to AWS ElasticBeanstalk')
parser.add_argument('--instance-type', action='store',
    help='Instance type of environment for create to AWS ElasticBeanstalk')
parser.add_argument('--load-balancer-type', action='store',
    help='Load balancer type of environment for create to AWS ElasticBeanstalk')
parser.add_argument('--shared-load-balancer', action='store', nargs='?',
    help='Shared load balancer of environment for create to AWS ElasticBeanstalk')
parser.add_argument('--use-spot', default=True, action=argparse.BooleanOptionalAction,
    help='Use spot of environment for create to AWS ElasticBeanstalk')
parser.add_argument('--use-isms-p', default=False, action=argparse.BooleanOptionalAction,
    help='Use isms-p of environment for create to AWS ElasticBeanstalk')
parser.add_argument('--use-pci-dss', default=False, action=argparse.BooleanOptionalAction,
    help='Use pci-dss of environment for create to AWS ElasticBeanstalk')
parser.add_argument('--tag-environment', action='store',
    help='Tag environment of environment for create to AWS ElasticBeanstalk')
parser.add_argument('--tag-part', action='store',
    help='Tag part of environment for create to AWS ElasticBeanstalk')
parser.add_argument('--tag-creator', action='store',
    help='Tag creator of environment for create to AWS ElasticBeanstalk')
args = parser.parse_args()

def get_client():
    """
    Get client for AWS ElasticBeanstalk
    """
    try:
        return boto3.client('elasticbeanstalk')
    except ClientError as err:
        print("Failed to create boto3 client.\n" + str(err))
        raise

def describe_application(client):
    """
    Describe application to AWS ElasticBeanstalk
    """
    try:
        response = client.describe_applications(
            ApplicationNames=[
                args.application_name
            ]
        )
    except ClientError as err:
        print("Failed to describe application.\n" + str(err))
        raise

    return len(response['Applications']) == 1

def create_application(client):
    """
    Create application to AWS ElasticBeanstalk
    """
    try:
        client.create_application(
            ApplicationName=args.application_name
        )
    except ClientError as err:
        print("Failed to create application.\n" + str(err))
        raise

    print('Application {application_name} is created.'.format(application_name=args.application_name))

def describe_application_version(client):
    """
    Describe application version to AWS ElasticBeanstalk
    """
    try:
        response = client.describe_application_versions(
            ApplicationName=args.application_name,
            VersionLabels=[
                'Sample Application'
            ]
        )
    except ClientError as err:
        print("Failed to describe application version.\n" + str(err))
        raise

    return len(response['ApplicationVersions']) == 1

def create_application_version(client):
    """
    Create application version to AWS ElasticBeanstalk
    """
    try:
        client.create_application_version(
            ApplicationName=args.application_name,
            VersionLabel='Sample Application'
        )
    except ClientError as err:
        print("Failed to create application version.\n" + str(err))
        raise

    print('Application version "Sample Application" is created.')

def describe_environment(client):
    """
    Describe environments in AWS ElasticBeanstalk
    """
    try:
        response = client.describe_environments(
            EnvironmentNames=[
                args.environment_name
            ]
        )
    except ClientError as err:
        print("Failed to describe environments.\n" + str(err))
        raise
    
    return len(response['Environments']) == 1

def describe_security_groups(classifier):
    """
    Describe security groups to AWS EC2
    """
    try:
        client = boto3.client('ec2')
    except ClientError as err:
        print("Failed to create boto3 client.\n" + str(err))
        raise

    filters = [
        {
            'Name': 'tag:Environment',
            'Value': [
                args.tag_environment
            ]
        },
        {
            'Name': 'tag:Classifier',
            'Value': [
                classifier
            ]
        }
    ]
    if classifier == 'chain':
        filters.append({
            'Name': 'tag:Part',
            'Value': [
                args.tag_part
            ]
        })

    try:
        response = client.describe_security_groups(
            Filters=filters
        )
    except ClientError as err:
        print("Failed to describe security groups.\n" + str(err))
        raise

    return response['SecurityGroups'][0]['GroupId']

def get_option_settings():
    """
    Get environment option settings to AWS ElasticBeanstalk
    """
    option_settings = []

    if args.use_spot:
        option_settings += [
            {
                'namespace': 'aws:ec2:instances',
                'name': 'SpotFleetOnDemandAboveBasePercentage',
                'value': '0'
            },
            {
                'namespace': 'aws:ec2:instances',
                'name': 'InstanceTypes',
                'value': args.instance_type
            },
            {
                'namespace': 'aws:ec2:instances',
                'name': 'EnableSpot',
                'value': 'true'
            },
            {
                'namespace': 'aws:autoscaling:asg',
                'name': 'EnableCapacityRebalancing',
                'value': 'true'
            }
        ]
    else:
        option_settings.append({
            'namespace': 'aws:autoscaling:launchconfiguration',
            'name': 'InstanceType',
            'value': args.instance_type
        })

    if args.load_balancer_type in ['application'] and args.shared_load_balancer:
        option_settings += [
            {
                'namespace': 'aws:elasticbeanstalk:environment',
                'name': 'LoadBalancerIsShared',
                'value': 'true'
            },
            {
                'namespace': 'aws:elbv2:loadbalancer',
                'name': 'SharedLoadBalancer',
                'value': args.shared_load_balancer
            }
        ]

    if args.use_pci_dss:
        chain_security_group = describe_security_groups('chain')
        option_settings += [
            {
                'namespace': 'aws:elbv2:loadbalancer',
                'name': 'ManagedSecurityGroup',
                'value': chain_security_group
            },
            {
                'namespace': 'aws:elbv2:loadbalancer',
                'name': 'SecurityGroups',
                'value': [chain_security_group, describe_security_groups('team')].join(',')
            }
        ]
    return option_settings

def get_tags():
    """
    Get environment tags to AWS ElasticBeanstalk
    """
    tags = {
        'Creator': args.tag_creator,
        'Service_owner':  args.tag_creator,
        'Auth_ismsp': args.use_isms_p
    }
    if args.use_pci_dss:
        tags.update({
            'Auth_pcidss': 'true',
            'Agent_ips': 'true'
        })

    return tags

def json_serial(object):
    """
    JSON serializer for objects not serializable by default json code
    """
    if isinstance(object, (datetime, date)):
        return object.isoformat()
    raise TypeError("Type %s not serializable" % type(object))

def json_format_dict(data, pretty=False):
    """
    Converts a dict to a JSON object and dumps it as a formatted string
    """
    if pretty:
        return json.dumps(data, sort_keys=True, indent=2, default=json_serial)
    else:
        return json.dumps(data, default=json_serial)

def main():
    client = get_client()

    if not describe_application(client):
        create_application(client)
    else:
        print('Application {application_name} already exists.'.format(application_name=args.application_name))

    if not describe_application_version(client):
        create_application_version(client)
    else:
        print('Application version "Sample Application" already exists.')

    if not describe_environment(client):
        open('/tmp/option_settings', 'w').write(json_format_dict(get_option_settings(), pretty=True))
        open('/tmp/tags', 'w').write(json_format_dict(get_tags(), pretty=True))
    else:
        sys.stderr.write('Environment {environment_name} already exists.'.format(environment_name=args.environment_name))
        sys.exit(1)

if __name__ == "__main__":
    main()