import boto3


class Function:
    def __init__(self, nome, method, bucket, role, arn):
        self.__nome = nome
        self.__method = method
        self.__arn = arn
        self.__bucket = bucket
        self.__role = role

        nome_function = self.__nome + self.__method
        nome_arquivo = nome_function + '.zip'

        self.__nome = nome_function

        client = boto3.client('lambda')

        response = client.create_function(
            Code={
                'S3Bucket': self.__bucket,
                'S3Key': nome_arquivo,
            },
            Description='#',
            FunctionName= nome_function,
            Handler= nome_function + '.lambda_handler',
            MemorySize=128,
            Publish=True,
            Role= self.__role,
            Runtime='python3.8',
            Timeout=3,
            TracingConfig={
                'Mode': 'PassThrough',
            },
        )

        arn_internal = response['FunctionArn']
        self.__arn = arn_internal
        
    @property
    def arn(self):
        return self.__arn

    @property
    def nome(self):
        return self.__nome