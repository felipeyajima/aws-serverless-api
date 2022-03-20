import boto3
import json
import botocore

def lambda_handler(event, context):
    from boto3.dynamodb.conditions import Key  
    table = boto3.resource("dynamodb").Table("loja")
    client = boto3.client('dynamodb')

    ordem = "ORDEM#" + event["pathParameters"]["id"]

    response = table.query(
        KeyConditionExpression=Key('PK').eq(ordem)
    )

    item = ''      

    if response["Count"] == 1:
        var_id = "ORDEM#" + event["pathParameters"]["id"]
        raw = event["body"]
        dados = json.loads(raw)
        var_valor = dados["VALOR"]
        var_data = dados["DATA"]
        var_cliente = "CLIENTE#" +  dados["CLIENTE"]

        response = client.update_item(
            ExpressionAttributeNames={
                '#V': 'VALOR',
                '#D': 'DATA',
                '#C': 'CLIENTE',
            },
            ExpressionAttributeValues={
                ':v': {
                    'S': var_valor,
                },
                ':d': {
                    'S': var_data,
                },
                ':c': {
                    'S': var_cliente,
                },
            },
            Key={
                'PK': {
                    'S': var_id,
                },
            },
            ReturnValues='ALL_NEW',
            TableName='loja',
            UpdateExpression='SET #V = :v, #D = :d, #C = :c',
        )
        return {
            'statusCode': 200,
            'body': json.dumps("Dados alterados")    
        }
    else:
        return {
            'statusCode': 404,
            'body': json.dumps('Ordem não Encontrada')    
        }  

