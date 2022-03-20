import json
import boto3

def lambda_handler(event, context):
    
    from boto3.dynamodb.conditions import Key
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('loja')

    PK = event['CPF']
    PK = "CLIENTE#" + PK
    EMAIL = event['EMAIL']
    CELULAR = event['CELULAR']
    NOME = event['NOME']
    
    
    #----- VERIFICAR SE O CLIENTE JA EXISTE -----

    response = table.query(
        KeyConditionExpression=Key('PK').eq(PK)
    )
    
    if response["Count"] == 1:
        item = response["Items"]
        return {"code":400, "message": "Cliente Existente"}
    else:


        if PK and EMAIL and CELULAR and NOME != '':
            vazio = False
        else:
            vazio = True
    
        if vazio == False: 
            EMAIL = EMAIL.lower()
            NOME = NOME.upper()
    
    
            dados_tratados = {'PK': PK, 'NOME': NOME, 'TIPO': 'CLIENTE', 'EMAIL': EMAIL, 'CELULAR': CELULAR}
    
            table.put_item(Item=dados_tratados)
            return {"code":200, "message": "Cliente adicionado com sucesso"}
    
        else: 
            return {"code":400, "message": "Solicitação inválida, falta de dados ou dados inválidos"}
