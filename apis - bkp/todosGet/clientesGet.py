import json
import boto3
import botocore

from boto3.dynamodb.conditions import Key
table = boto3.resource("dynamodb").Table("loja")

resp = table.query(
    IndexName="TIPO-index",
    KeyConditionExpression=Key('TIPO').eq('CLIENTE')
)