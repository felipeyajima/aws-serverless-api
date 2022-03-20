import boto3
import json

class Dynamodb:
    def __init__(self, nome_tabela, arn):
        
        self.__nome_tabela = nome_tabela
        self.__arn = arn


    def cria_tabela(self):
        
        self.__nome_tabela
        
        dynamodb = boto3.resource('dynamodb')

        table = dynamodb.create_table(
            TableName=self.__nome_tabela,
            # Define as chaves primarias HASH e RANGE
            KeySchema=[
                {
                    'AttributeName': 'PK',
                    'KeyType': 'HASH'
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'PK',
                    'AttributeType': 'S'
                }
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        )

        # Wait until the table exists.
        table.meta.client.get_waiter('table_exists').wait(TableName=self.__nome_tabela)
        # Print out some data about the table.
        print(table.item_count)

        self.__arn = table.table_arn

    
    def popula_tabela(self):
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table(self.__nome_tabela)
        with table.batch_writer() as batch:
            batch.put_item(
                Item={
                    "PK" : "CLIENTE#00000000001",
                    "NOME" : "FELIPE",
                    "EMAIL" : "felipe.yajimabatista@gmail.com",
                    "CELULAR" : "+55 11 970630909",
                    "TIPO" : "CLIENTE"
                }
            ),

            batch.put_item(
                Item={
                    "PK" : "CLIENTE#00000000002",
                    "NOME" : "RODRIGO",
                    "EMAIL" : "felipe.yajimabatista@gmail.com",
                    "CELULAR" : "+55 11 970630909",
                    "TIPO" : "CLIENTE"
                }
            ),

            batch.put_item(
                Item={
                    "PK" : "PRODUTO#14",
                    "MARCA" : "CASIO",
                    "MODELO" : "TC50",
                    "PRECO" : "1500",
                    "PRODUTO" : "TECLADO MUSICAL",
                    "TIPO" : "PRODUTO"
                }
            ),

            batch.put_item(
                Item={
                    "PK" : "PRODUTO#15",
                    "MARCA" : "TAGIMA",
                    "MODELO" : "GY05",
                    "PRECO" : "1800",
                    "PRODUTO" : "GUITARRA ELETRICA",
                    "TIPO" : "PRODUTO"
                }
            ),

            batch.put_item(
                Item={
                    "PK" : "ORDEM#001",
                    "CLIENTE" : "CLIENTE#00000000001",
                    "TIPO" : "ORDEM",
                    "VALOR" : "2511",
                    "PRODUTO1" : "PRODUTO#14",
                    "PRODUTO2" : "PRODUTO#15"
                }
            ),

            batch.put_item(
                Item={
                    "PK" : "ORDEM#002",
                    "CLIENTE" : "CLIENTE#00000000002",
                    "TIPO" : "ORDEM",
                    "VALOR" : "2511",
                    "PRODUTO1" : "PRODUTO#14",
                    "PRODUTO2" : "PRODUTO#15"
                }
            )


        return self.__nome_tabela
    '''
    def cria_gsi(self):
        client = boto3.client('dynamodb')
        response = client.update_table(
            AttributeDefinitions=[
                {
                    'AttributeName': 'TERCEIRA-PK',
                    'AttributeType': 'S'
                }
            ],
            TableName=self.__nome_tabela,
            GlobalSecondaryIndexUpdates=[
                {
                    'Create': {
                        'IndexName': 'TERCEIRA-PK-index',
                        'KeySchema': [
                            {
                                'AttributeName': 'TERCEIRA-PK',
                                'KeyType': 'HASH'
                            }
                        ],
                        'Projection': {
                            'ProjectionType': 'ALL'
                        },
                        'ProvisionedThroughput': {
                            'ReadCapacityUnits': 5,
                            'WriteCapacityUnits': 5
                        }
                    }
                }
            ]
        )
    '''
    def cria_gsi2(self):
        client = boto3.client('dynamodb')
        response = client.update_table(
            AttributeDefinitions=[
                {
                    'AttributeName': 'TIPO',
                    'AttributeType': 'S'
                }
            ],
            TableName=self.__nome_tabela,
            GlobalSecondaryIndexUpdates=[
                {
                    'Create': {
                        'IndexName': 'TIPO-index',
                        'KeySchema': [
                            {
                                'AttributeName': 'TIPO',
                                'KeyType': 'HASH'
                            }
                        ],
                        'Projection': {
                            'ProjectionType': 'ALL'
                        },
                        'ProvisionedThroughput': {
                            'ReadCapacityUnits': 5,
                            'WriteCapacityUnits': 5
                        }
                    }
                }
            ]
        )
    
    @property
    def nome(self):
        return self.__nome_tabela

    @property
    def arn(self):
        return self.__arn