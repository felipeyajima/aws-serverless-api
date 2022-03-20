import json
import boto3
import botocore

def lambda_handler(event, context):

    from boto3.dynamodb.conditions import Key
    client = boto3.client('dynamodb')
    table = boto3.resource("dynamodb").Table("loja")
    produto = "PRODUTO#" + event["pathParameters"]["id"]

    resp = table.query(
        KeyConditionExpression=Key('PK').eq(produto)
    )

    if resp["Count"] == 1:
        response = client.delete_item(
            Key={
                'PK': {
                    'S': produto,
                }
            },
            TableName='loja'
        )

        return {
            'statusCode': 200,
            'body': json.dumps('Produto deletado')    
        }
    else:
        return {
            'statusCode': 404,
            'body': json.dumps('Produto nao encontrado')
        }
