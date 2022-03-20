import boto3
import json
import botocore


client = boto3.client('dynamodb')


response = client.update_item(
    ExpressionAttributeNames={
        '#C': 'CELULAR',
        '#E': 'EMAIL',
        '#N': 'NOME',
    },
    ExpressionAttributeValues={
        ':c': {
            'S': '+55 11 9070555555',
        },
        ':e': {
            'S': 'felipe@yajima.com.br',
        },
        ':n': {
            'S': 'ROBSON',
        },
    },
    Key={
        'PK': {
            'S': 'CLIENTE#00000000001',
        },
    },
    ReturnValues='ALL_NEW',
    TableName='loja',
    UpdateExpression='SET #C = :c, #E = :e, #N = :n',
)

print(response)