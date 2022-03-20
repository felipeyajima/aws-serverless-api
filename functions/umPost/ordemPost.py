import json
import boto3
import random

def lambda_handler(event, context):
    
    from boto3.dynamodb.conditions import Key
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('loja')

    PK = random.randrange(1, 100)
    PK = "ORDEM#" + str(PK)
    CLIENTE = event['CPF']
    CLIENTE = "CLIENTE#" + CLIENTE
    DATA = event['DATA']
    PRODUTO1 = event['PRODUTO1']
    PRODUTO2 = event['PRODUTO2']
    VALOR = event['VALOR']
    
    #----- VERIFICAR SE O CLIENTE JA EXISTE -----

    response = table.query(
        KeyConditionExpression=Key('PK').eq(PK)
    )
    
    if response["Count"] == 1:
        item = response["Items"]
        return {"code":400, "message": "Ordem Existente"}
    else:


        if PK and CLIENTE and DATA and PRODUTO1 and PRODUTO2 and VALOR != '':
            vazio = False
        else:
            vazio = True
    
        if vazio == False: 

            dados_tratados = {'PK': PK, 'CLIENTE': CLIENTE, 'TIPO': 'ORDEM', 'DATA': DATA, 'VALOR': VALOR, 'PRODUTO1': PRODUTO1, 'PRODUTO2': PRODUTO2}
    
            table.put_item(Item=dados_tratados)
            return {"code":200, "message": "Ordem adicionada com sucesso"}
    
        else: 
            return {"code":400, "message": "Solicitação inválida, falta de dados ou dados inválidos"}
