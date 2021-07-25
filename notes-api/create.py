import json
import uuid
import boto3
from datetime import datetime


def main(event, context):

    dynamodb = boto3.resource('dynamodb')
    data = json.loads(event['body'])

    table = dynamodb.Table('notes')

    item = {
      'userId': event['requestContext']['identity']['cognitoIdentityId'],
      'noteId': str(uuid.uuid4()),
      'content': data['content'],
      'attachment': data['attachment'],
      'createdAt': str(datetime.now()),
    }

    table.put_item(Item=item)

    response = {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Credentials": True,
        },
        "body": json.dumps(item)
    }

    return response
