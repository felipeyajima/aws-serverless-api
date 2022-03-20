import boto3
import json


class Policy_Lambda:
    def __init__(self, politica_nome, politica_arn):
        print('Construindo a politica {}'.format(self))

        self.__politica_nome = politica_nome
        self.__politica_arn = politica_arn
        
        iam = boto3.client('iam')

        policy = {
            "Version": "2012-10-17",
            "Statement": 
            {
                "Effect": "Allow",
                "Action": "lambda:*",
                "Resource": "*"
            }
        }

        response = iam.create_policy(
        PolicyName=self.__politica_nome,
        PolicyDocument=json.dumps(policy)
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

    


