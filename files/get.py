import os
import json

import boto3
dynamodb = boto3.resource('dynamodb')

def get(event, context):
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    # fetch todo from the database
    result = table.get_item(
        Key={
            'id': event['id']
        }
    )

    # create a response
    response = {
        "statusCode": 200,
        "body": result['Item']
    }

    return response