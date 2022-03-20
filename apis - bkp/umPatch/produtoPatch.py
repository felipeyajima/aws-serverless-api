import boto3
import json
import botocore


client = boto3.client('dynamodb')


response = client.update_item(
    ExpressionAttributeNames={
        '#M': 'MARCA',
        '#O': 'MODELO',
        '#T': 'PRODUTO',
        '#P': 'PRECO',
    },
    ExpressionAttributeValues={
        ':m': {
            'S': 'CASIO',
        },
        ':o': {
            'S': 'TC50',
        },
        ':t': {
            'S': 'TECLADO MUSICAL',
        },
        ':p': {
            'N': '1400',
        },
    },
    Key={
        'PK': {
            'S': 'PRODUTO#001',
        },
    },
    ReturnValues='ALL_NEW',
    TableName='loja',
    UpdateExpression='SET #M = :m, #O = :o, #T = :t, #P = :p',
)

print(response)