import json
import boto3
import botocore

def lambda_handler(event, context):

  from boto3.dynamodb.conditions import Key
  table = boto3.resource("dynamodb").Table("loja")

  produto = "PRODUTO#" + event["pathParameters"]["id"]

  response = table.query(
    KeyConditionExpression=Key('PK').eq(produto)
  )

  item = ''

  if response["Count"] == 1:
    item = response["Items"]
    return {
      'statusCode': 200,
      'body': json.dumps(item)    
    }
  else:
    return {
      'statusCode': 404,
      'body': json.dumps('Produto não Encontrado')    
    }  