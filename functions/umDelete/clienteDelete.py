import json
import boto3
import botocore

def lambda_handler(event, context):

    from boto3.dynamodb.conditions import Key
    client = boto3.client('dynamodb')
    table = boto3.resource("dynamodb").Table("loja")
    cliente = "CLIENTE#" + event["pathParameters"]["id"]

    resp = table.query(
        KeyConditionExpression=Key('PK').eq(cliente)
    )

    if resp["Count"] == 1:
        response = client.delete_item(
            Key={
                'PK': {
                    'S': cliente,
                }
            },
            TableName='loja'
        )

        return {
            'statusCode': 200,
            'body': json.dumps('Cliente deletado')    
        }
    else:
        return {
            'statusCode': 404,
            'body': json.dumps('Cliente não Encontrado')
        }
