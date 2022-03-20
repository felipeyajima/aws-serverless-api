import json
import boto3
import random

def lambda_handler(event, context):
    
    from boto3.dynamodb.conditions import Key
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('loja')

    PK = random.randrange(1, 100)
    PK = "PRODUTO#" + str(PK)
    MARCA = event['MARCA']
    MODELO = event['MODELO']
    PRECO = event['PRECO']
    PRODUTO = event['PRODUTO']
    
    #----- VERIFICAR SE O CLIENTE JA EXISTE -----

    response = table.query(
        KeyConditionExpression=Key('PK').eq(PK)
    )
    
    if response["Count"] == 1:
        item = response["Items"]
        return {"code":400, "message": "Produto Existente"}
    else:


        if MARCA and MODELO and PRECO and PRODUTO != '':
            vazio = False
        else:
            vazio = True
    
        if vazio == False: 

            dados_tratados = {'PK': PK, 'MARCA': MARCA, 'MODELO': MODELO, 'TIPO': 'PRODUTO', 'PRECO': PRECO, 'PRODUTO': PRODUTO}
    
            table.put_item(Item=dados_tratados)
            return {"code":200, "message": "Produto adicionado com sucesso"}
    
        else: 
            return {"code":400, "message": "Solicitação inválida, falta de dados ou dados inválidos"}
