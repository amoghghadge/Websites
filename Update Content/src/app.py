import boto3
import json
import os
import base64
import email.parser
from requests_toolbelt.multipart import decoder
from cgi import parse_multipart, parse_header
from io import BytesIO
import re

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

s3 = boto3.client("s3")

def lambda_handler(event, context):

    # type: bytes
    decoded_form = base64.b64decode(event.get("body-json"))

    print(decoded_form)

    # type: string

    try:
        form_string = decoded_form.decode('utf-8')
    except:
        form_string = decoded_form.decode('utf-8')

    pattern = re.compile(r'filename="\w+\.\w+"')

    file_names = pattern.findall(form_string)
    for x in range(len(file_names)):
        # print(type(file_names[x]), file_names[x])
        file_names[x] = file_names[x][10:len(file_names[x])-1]



    content_type = event["params"]['header']['Content-Type']
    c_type, c_data = parse_header(content_type)


    c_data['boundary'] = bytes(c_data['boundary'], "utf-8")


    form_data = parse_multipart(BytesIO(decoded_form), c_data)

    file_bodies = []

    for file_body in form_data['website-files']:
        file_body = file_body.decode('utf-8')
        file_bodies.append(file_body)
    
    for x in range(len(file_names)):
        s3_upload = s3.put_object(Bucket="aghadge-functionoutput", Key=file_names[x], Body=file_bodies[x], ExtraArgs={'ACL': 'public-read'})

    return "Uploaded files to S3!"