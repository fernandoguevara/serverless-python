import json
import boto3
from datetime import datetime
import uuid


def main(event, context):
    dynamodb = boto3.resource('dynamodb')
    data = json.loads(event['body'])

    table = dynamodb.Table('notes')

    item = table.update_item(
        Key={
            'userId': event['requestContext']['identity']['cognitoIdentityId'],
            'noteId': event['pathParameters']['id']
        },
        UpdateExpression="SET content = :content, attachment = :attachment",
        ExpressionAttributeValues={
            ":attachment": data['attachment'],
            ":content": data['content'],

        },
        ReturnValues="ALL_NEW"
    )

    response = {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Credentials": True,
        },
        "body": json.dumps(item)
    }

    return response
