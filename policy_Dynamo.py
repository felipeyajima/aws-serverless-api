import boto3
import json


class Policy_Dynamo:
    def __init__(self, politica_nome, tabela_nome, tabela_arn, politica_arn):
        print('Construindo a politica {}'.format(self))

        self.__politica_nome = politica_nome
        self.__tabela_nome = tabela_nome
        self.__tabela_arn = tabela_arn
        self.__politica_arn = politica_arn
        
        iam = boto3.client('iam')

        
        my_managed_policy = {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Effect": "Allow",
                    "Action": "logs:CreateLogGroup",
                    "Resource": [
                        self.__tabela_arn,
                        "arn:aws:dynamodb:*:*:table/*/index/*"
                    ]
                },
                {
                    "Effect": "Allow",
                    "Action": [
                        "dynamodb:DeleteItem",
                        "dynamodb:GetItem",
                        "dynamodb:PutItem",
                        "dynamodb:Scan",
                        "dynamodb:Query",
                        "dynamodb:UpdateItem"
                    ],
                    "Resource": [
                        self.__tabela_arn,
                        "arn:aws:dynamodb:*:*:table/*/index/*"
                    ]
                }
            ]
        }

        response = iam.create_policy(
            PolicyName=self.__politica_nome,
            PolicyDocument=json.dumps(my_managed_policy)
        )
        #print(response)

        print('ARN DA POLITICA EH {}'.format(response['Policy']['Arn']))

        arn_politica = response['Policy']['Arn']
        self.__politica_arn = arn_politica

        #Pegando o nome da Policy
        #nome_policy = response['Policy']['Arn']

    @property
    def nome(self):
        return self.__politica_nome
    
    @property
    def arn(self):
        return self.__politica_arn

    


