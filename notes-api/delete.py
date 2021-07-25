import json
import boto3
from datetime import datetime
import uuid

def main(event, context):

    dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('notes')

    table.delete_item(
        Key={
            'userId': event['requestContext']['identity']['cognitoIdentityId'],
            'noteId': event['pathParameters']['id']
        },
    )

    response = {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Credentials": True,
        },
        "body": True
    }

    return response