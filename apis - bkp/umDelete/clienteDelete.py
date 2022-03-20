import json
import boto3
import botocore

from boto3.dynamodb.conditions import Key
client = boto3.client('dynamodb')
table = boto3.resource("dynamodb").Table("loja")


resp = table.query(
    KeyConditionExpression=Key('PK').eq('CLIENTE#00000000001')
)

if resp["Count"] == 1:
    response = client.delete_item(
        Key={
            'PK': {
                'S': 'CLIENTE#00000000001',
            }
        },
        TableName='loja'
    )
    status_code="200" 
else:
    status_code="404"

