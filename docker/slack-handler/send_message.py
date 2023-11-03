#!/usr/bin/env python

from __future__ import print_function
from datetime import date, datetime
import os
import json
import argparse
import requests

parser = argparse.ArgumentParser(
    description='Configures user so that you can retrieve to Slack')
parser.add_argument('--user-email', action='store', nargs='?',
    help='Email of user for retrieve to Slack')
parser.add_argument('--attachment', action='store',
    help='Attachment of message for retrieve to Slack')
args = parser.parse_args()

def get_user_id():
    """
    Get user id to Slack
    """
    response = requests.get(
        '{slack_api_url}/api/users.lookupByEmail'.format(slack_api_url=os.environ.get('SLACK_API_URL', 'https://slack.com')), 
        params={
            'token': os.environ.get('SLACK_TOKEN'),
            'email': args.user_email
        }).json()

    if response['ok']:
        return response['user']['id']
    else:
        return ''

def send_message(user_id):
    """
    Send message to Slack
    """
    attachment = json.loads(args.attachment)

    if user_id:
        attachment['pretext'] = '<@{user_id}> {pretext}'.format(user_id=user_id, pretext=attachment['pretext'])

    payload = {
        'attachments': [
            attachment
        ],
        'mrkdwn': [
            'pretext',
            'text',
            'fields'
        ],
        'icon_emoji': os.environ.get('SLACK_ICON_EMOJI'),
        'username': os.environ.get('SLACK_USER_NAME'),
        'channel': os.environ.get('SLACK_CHANNEL')
    }
    requests.post(
        os.environ.get('SLACK_WEBHOOK_URL'), 
        data=json_format_dict(payload, pretty=True))

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
    user_id = ''

    if args.user_email:
        user_id = get_user_id()

    send_message(user_id)

if __name__ == "__main__":
    main()