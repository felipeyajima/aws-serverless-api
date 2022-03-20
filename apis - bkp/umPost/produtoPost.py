import json
import boto3
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('loja')

PK = 'PRODUTO#003'
PRODUTO = 'GUITARRA'
PRECO = 1550
TIPO = 'PRODUTO'
MARCA = 'TAGIMA'
MODELO = 'G02'

dados_tratados = {'PK': PK, 'PRODUTO': PRODUTO, 'PRECO': PRECO, 'TIPO': TIPO, 'MARCA': MARCA, 'MODELO': MODELO}

table.put_item(Item=dados_tratados)
