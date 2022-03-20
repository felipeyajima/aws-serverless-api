import boto3
import json
import botocore

def lambda_handler(event, context):
    from boto3.dynamodb.conditions import Key  
    table = boto3.resource("dynamodb").Table("loja")
    client = boto3.client('dynamodb')

    cliente = "CLIENTE#" + event["pathParameters"]["id"]

    response = table.query(
        KeyConditionExpression=Key('PK').eq(cliente)
    )

    item = ''    

    if response["Count"] == 1:
        var_id = "CLIENTE#" + event["pathParameters"]["id"]
        raw = event["body"]
        dados = json.loads(raw)
        var_email = dados["EMAIL"]
        var_celular = dados["CELULAR"]
        var_nome = dados["NOME"]

        response = client.update_item(
            ExpressionAttributeNames={
                '#C': 'CELULAR',
                '#E': 'EMAIL',
                '#N': 'NOME',
            },
            ExpressionAttributeValues={
                ':c': {
                    'S': var_celular,
                },
                ':e': {
                    'S': var_email,
                },
                ':n': {
                    'S': var_nome,
                },
            },
            Key={
                'PK': {
                    'S': var_id,
                },
            },
            ReturnValues='ALL_NEW',
            TableName='loja',
            UpdateExpression='SET #C = :c, #E = :e, #N = :n',
        )
        return {
            'statusCode': 200,
            'body': json.dumps("Dados alterados")    
        }
    else:
        return {
            'statusCode': 404,
            'body': json.dumps('Cliente não Encontrado')    
        }  

    
