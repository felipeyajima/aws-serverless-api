import boto3
import json
import botocore


client = boto3.client('dynamodb')


response = client.update_item(
    ExpressionAttributeNames={
        '#V': 'VALOR',
        '#D': 'DATA',
        '#C': 'CLIENTE',
    },
    ExpressionAttributeValues={
        ':v': {
            'N': '1500',
        },
        ':d': {
            'S': '20191212',
        },
        ':c': {
            'S': 'CLIENTE#00000000004',
        },
    },
    Key={
        'PK': {
            'S': 'ORDEM#001',
        },
    },
    ReturnValues='ALL_NEW',
    TableName='loja',
    UpdateExpression='SET #V = :v, #D = :d, #C = :c',
)

print(response)