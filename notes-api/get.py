import json
import boto3
from datetime import datetime
import uuid

def main(event, context):

    dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('notes')

    key = {'userId': event['requestContext']['identity']['cognitoIdentityId'],
           'noteId': event['pathParameters']['id']}

    result = table.get_item(Key=key)

    response = {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Credentials": True,
        },
        "body": json.dumps(result)
    }

    return response

