import json
import boto3
from datetime import datetime
import uuid


def main(event, context):
    dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('notes')

    result = table.scan()

    response = {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Credentials": True,
        },
        "body": json.dumps(result)
    }

    return response
