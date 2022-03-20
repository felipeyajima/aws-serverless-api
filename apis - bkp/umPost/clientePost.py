import json
import boto3
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('loja')

PK = 'CLIENTE#00000000003'
NOME = 'JULIANO'
TIPO = 'CLIENTE'
EMAIL = 'felipe.yajimabatista@gmail.com'
CELULAR = '+55 11 970630909'

dados_tratados = {'PK': PK, 'NOME': NOME, 'TIPO': TIPO, 'EMAIL': EMAIL, 'CELULAR': CELULAR}

table.put_item(Item=dados_tratados)

