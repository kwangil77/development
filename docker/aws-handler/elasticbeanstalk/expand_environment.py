#!/usr/bin/env python

from __future__ import print_function
from datetime import timedelta
from time import sleep
import argparse
import boto3
from botocore.exceptions import ClientError

parser = argparse.ArgumentParser(
    description='Configures environment so that you can update to AWS ElasticBeanstalk')
parser.add_argument('--environment-names', action='store', nargs='+',
    help='The names of the environment for update to AWS ElasticBeanstalk')
parser.add_argument('--version-label', action='store',
    help='The label of application version for update to AWS ElasticBeanstalk')
parser.add_argument('--environment-cname', action='store',
    help='The cname of the environment for update to AWS ElasticBeanstalk')
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

def describe_environments(client):
    """
    Describe environments in AWS ElasticBeanstalk
    """
    try:
        response = client.describe_environments(
            EnvironmentNames=[
                args.environment_names[0]
            ]
        )
    except ClientError as err:
        print("Failed to describe environments.\n" + str(err))
        raise
    
    environment = response['Environments'][0]
    return environment['ApplicationName'], args.environment_names[1] if str(environment['CNAME']) == args.environment_cname else args.environment_names[0]

def describe_configuration_settings(client, application_name, environment_name):
    """
    Describe environment settings in AWS ElasticBeanstalk
    """
    try:
        response = client.describe_configuration_settings(
            ApplicationName=application_name,
            EnvironmentName=environment_name
        )
    except ClientError as err:
        print("Failed to describe environment settings.\n" + str(err))
        raise
    
    options = []
    
    if len(response['ConfigurationSettings']) == 1:
        for option in response['ConfigurationSettings'][0]['OptionSettings']:
            if str(option['Namespace']) == 'aws:autoscaling:asg':
                if str(option['OptionName']) == 'MinSize':
                    options.append({
                        'ResourceName': 'AWSEBAutoScalingGroup',
                        'Namespace': 'aws:autoscaling:asg',
                        'OptionName': 'MinSize',
                        'Value': str(option['Value'])
                    })
                elif str(option['OptionName']) == 'MaxSize':
                    options.append({
                        'ResourceName': 'AWSEBAutoScalingGroup',
                        'Namespace': 'aws:autoscaling:asg',
                        'OptionName': 'MaxSize',
                        'Value': str(option['Value'])
                    })
    else:
        print("Failed to describe environment settings.\n" + str(err))
        raise

    return options

def update_environment(client, environment_name, options = None):
    """
    Update environment to AWS ElasticBeanstalk
    """
    try:
        if options is None:
            client.update_environment(
                EnvironmentName=environment_name,
                VersionLabel=args.version_label
            )
        else:
            client.update_environment(
                EnvironmentName=environment_name,
                OptionSettings=options
            )
    except ClientError as err:
        print("Failed to update environment.\n" + str(err))
        raise

def describe_environment(client, environment_name):
    """
    Describe environments in AWS ElasticBeanstalk
    """
    try:
        response = client.describe_environments(
            EnvironmentNames=[
                environment_name
            ]
        )
    except ClientError as err:
        print("Failed to describe environments.\n" + str(err))
        raise
    
    return str(response['Environments'][0]['VersionLabel']) == args.version_label and str(response['Environments'][0]['Status']) == 'Ready'

def describe_events(client, environment_name, start_time = None):
    """
    Describe events in AWS ElasticBeanstalk
    """
    response = dict(Events=[])

    try:
        if start_time is None:
            response = client.describe_events(
                EnvironmentName=environment_name,
                MaxRecords=1
            )
        else:
            response = client.describe_events(
                EnvironmentName=environment_name,
                StartTime=start_time
            )
    except ClientError as err:
        print("Failed to describe events.\n" + str(err))
        raise

    for event in reversed(response['Events']):
        if start_time is None or event['EventDate'] > start_time:
            start_time = event['EventDate']
        print(str(event['EventDate']) + ' [' + str(event['Severity']) + '] ' + str(event['Message']))
    
    return start_time + timedelta(seconds=1)

def main():
    client = get_client()
    application_name, environment_name = describe_environments(client)
    open('/tmp/environment_name', 'w').write(environment_name)

    update_environment(client, environment_name)
    start_time = describe_events(client, environment_name)

    while not describe_environment(client, environment_name):
        sleep(20)
        start_time = describe_events(client, environment_name, start_time)

    describe_events(client, environment_name, start_time)

    options = describe_configuration_settings(client, application_name, args.environment_names[1] if args.environment_names[0] == environment_name else args.environment_names[0])
    update_environment(client, environment_name, options)

    while not describe_environment(client, environment_name):
        sleep(20)
        start_time = describe_events(client, environment_name, start_time)

    describe_events(client, environment_name, start_time)

if __name__ == "__main__":
    main()