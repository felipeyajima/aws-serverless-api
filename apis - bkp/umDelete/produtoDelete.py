import json
import boto3
import botocore

from boto3.dynamodb.conditions import Key
client = boto3.client('dynamodb')
table = boto3.resource("dynamodb").Table("loja")


resp = table.query(
    KeyConditionExpression=Key('PK').eq('PRODUTO#001')
)

if resp["Count"] == 1:
    response = client.delete_item(
        KeyConditionExpression=Key('PK').eq('PRODUTO#001')
    )
    status_code="200" 
else:
    status_code="404"


if resp["Count"] == 1:
    response = client.delete_item(
        Key={
            'PK': {
                'S': 'PRODUTO#001',
            },
        },
        TableName='loja'
    )
    status_code="200" 
else:
    status_code="404"
