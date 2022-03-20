import boto3
import json

class Role_APIGateway_Lambda:
    def __init__(self, role_nome, policy_arn, role_arn):
        self.__role_nome = role_nome
        self.__policy_arn = policy_arn
        self.__role_arn = role_arn

        iam = boto3.client('iam')

        document = {'Version': '2012-10-17', 
            'Statement': [
                {
                    'Effect': 'Allow', 
                    'Principal': {
                        'Service': 'apigateway.amazonaws.com'
                    }, 
                    'Action': 'sts:AssumeRole'
                }
            ]
        }
        jasondocument=json.dumps(document,indent=4)

        response = iam.create_role(
            Path='/',
            RoleName=self.__role_nome,
            AssumeRolePolicyDocument=jasondocument,
            MaxSessionDuration=3600,
            PermissionsBoundary=self.__policy_arn,
            Tags=[
                {
                    'Key': 'Depto',
                    'Value': 'Cloud'
                }
            ]
        )

        self.__role_arn = response['Role']['Arn']

        #atachando a policy na role criada
        iam.attach_role_policy(
            PolicyArn=self.__policy_arn,
            RoleName=self.__role_nome
        )

    @property
    def nome(self):
        return self.__role_nome

    @property
    def arn(self):
        return self.__role_arn
