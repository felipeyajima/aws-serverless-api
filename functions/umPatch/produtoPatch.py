import boto3
import json
import botocore

def lambda_handler(event, context):
    from boto3.dynamodb.conditions import Key  
    table = boto3.resource("dynamodb").Table("loja")
    client = boto3.client('dynamodb')

    produto = "PRODUTO#" + event["pathParameters"]["id"]

    response = table.query(
        KeyConditionExpression=Key('PK').eq(produto)
    )

    item = ''


    if response["Count"] == 1:
        var_id = "PRODUTO#" + event["pathParameters"]["id"]
        raw = event["body"]
        dados = json.loads(raw)
        var_marca = dados["MARCA"]
        var_modelo = dados["MODELO"]
        var_produto = dados["PRODUTO"]
        var_preco = dados["PRECO"]

        response = client.update_item(
            ExpressionAttributeNames={
                '#M': 'MARCA',
                '#O': 'MODELO',
                '#T': 'PRODUTO',
                '#P': 'PRECO',
            },
            ExpressionAttributeValues={
                ':m': {
                    'S': var_marca,
                },
                ':o': {
                    'S': var_modelo,
                },
                ':t': {
                    'S': var_produto,
                },
                ':p': {
                    'S': var_preco,
                },
            },
            Key={
                'PK': {
                    'S': var_id,
                },
            },
            ReturnValues='ALL_NEW',
            TableName='loja',
            UpdateExpression='SET #M = :m, #O = :o, #T = :t, #P = :p',
        )

        return {
            'statusCode': 200,
            'body': json.dumps("Dados alterados")    
        }
    else:
        return {
            'statusCode': 404,
            'body': json.dumps('Produto não Encontrado')    
        }          

