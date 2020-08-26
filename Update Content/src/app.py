import boto3
import json
import os

print('Loading function')

# Response for API Lambda proxy

# def respond(err, res=None):
#     return {
#         'statusCode': '400' if err else '200',
#         'body': err.message if err else json.dumps(res),
#         'headers': {
#             'Content-Type': 'application/json',
#         },
#     }


def lambda_handler(event, context):
    print(event)
    return event.get('key1')
