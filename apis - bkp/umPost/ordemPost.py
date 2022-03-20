import json
import boto3
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('loja')

PK = 'ORDEM#003'
CLIENTE = 'CLIENTE#00000000002'
TIPO = 'ORDEM'
DATA = '20200505'
VALOR = 1500

dados_tratados = {'PK': PK, 'CLIENTE': CLIENTE, 'TIPO': TIPO, 'DATA': DATA, 'VALOR': VALOR}

table.put_item(Item=dados_tratados)