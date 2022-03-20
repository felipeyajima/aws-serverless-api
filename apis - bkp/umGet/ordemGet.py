import json
import boto3
import botocore

from boto3.dynamodb.conditions import Key
table = boto3.resource("dynamodb").Table("loja")

response = table.query(
  KeyConditionExpression=Key('PK').eq('ORDEM#001')
)
