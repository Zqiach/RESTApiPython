import json
import logging
import os
import time
import uuid
from datetime import datetime
import boto3

dynamodb = boto3.resource('dynamodb')


def create(event, context):
    data = json.loads(event['body'])
    if 'text' not in data:
        logging.error("Validation Failed")
        raise Exception("Couldn't create the restClient item, no data included in text field")

    timestamp = str(datetime.utcnow().timestamp())
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])
    item = {
        'id': str(uuid.uuid1()),
        'text': data['text'],
    }

    table.put_item(Item=item)
    response = {
        "statusCode": 200,
        "body": json.dumps(item)
    }

    return response
