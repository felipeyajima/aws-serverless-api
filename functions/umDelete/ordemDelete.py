import json
import boto3
import botocore

def lambda_handler(event, context):

    from boto3.dynamodb.conditions import Key
    client = boto3.client('dynamodb')
    table = boto3.resource("dynamodb").Table("loja")
    ordem = "ORDEM#" + event["pathParameters"]["id"]

    resp = table.query(
        KeyConditionExpression=Key('PK').eq(ordem)
    )

    if resp["Count"] == 1:
        response = client.delete_item(
            Key={
                'PK': {
                    'S': ordem,
                }
            },
            TableName='loja'
        )

        return {
            'statusCode': 200,
            'body': json.dumps('Ordem Deletada')    
        }
    else:
        return {
            'statusCode': 404,
            'body': json.dumps('Ordem Não Encontrada')
        }
