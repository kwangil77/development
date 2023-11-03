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
parser.add_argument('--environment-name', action='store',
    help='The name of the environment for update to AWS ElasticBeanstalk')
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

def swap_environment_cnames(client, environment_name):
    """
    Swap environment cnames to AWS ElasticBeanstalk
    """
    try:
        client.swap_environment_cnames(
            SourceEnvironmentName=args.environment_name,
            DestinationEnvironmentName=environment_name
        )
    except ClientError as err:
        print("Failed to swap environment cnames.\n" + str(err))
        raise

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
    
    return str(response['Environments'][0]['Status']) == 'Ready'

def describe_events(client, start_time = None):
    """
    Describe events in AWS ElasticBeanstalk
    """
    response = dict(Events=[])

    try:
        if start_time is None:
            response = client.describe_events(
                EnvironmentName=args.environment_name,
                MaxRecords=1
            )
        else:
            response = client.describe_events(
                EnvironmentName=args.environment_name,
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
    environment_name = args.environment_names[1] if args.environment_names[0] == args.environment_name else args.environment_names[0]
    open('/tmp/environment_name', 'w').write(environment_name)

    swap_environment_cnames(client, environment_name)
    start_time = describe_events(client)

    while not describe_environment(client):
        sleep(20)
        start_time = describe_events(client, start_time)

    describe_events(client, start_time)

if __name__ == "__main__":
    main()