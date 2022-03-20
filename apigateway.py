import boto3
client = boto3.client('apigateway')

class Rest:
    def __init__(self, nome, id, barra):
        self.__nome = nome
        self.__id = id
        self.__barra = barra

        response = client.create_rest_api(
            name=self.__nome,
            apiKeySource='HEADER',
            endpointConfiguration={
                'types': [
                    'REGIONAL',
                ]
            }
        )

        response

        # Pegando o ID da RestApi recem criada
        response1 = client.get_rest_apis()
        id_rest = response1['items'][0]['id']
        self.__id = id_rest

        # Pegando o ID do Barra
        response2 = client.get_resources(
            restApiId=self.__id
        )
        id_resource = response2['items'][0]['id']
        self.__barra = id_resource

    @property
    def nome(self):
        return self.__nome


    @property
    def id(self):
        return self.__id

    @property
    def barra(self):
        return self.__barra



class Resource:
    def __init__(self, nome, rest_id, rest_barra, resource_id):

        self.__nome = nome
        self.__rest_api_id = rest_id
        self.__parent_id = rest_barra
        self.__resource_id = resource_id

        response = client.create_resource(
            restApiId=self.__rest_api_id,
            parentId=self.__parent_id,
            pathPart=self.__nome
        )

        self.__resource_id = response['id']

    @property
    def nome(self):
        return self.__nome

    @property
    def resource_id(self):
        return self.__resource_id


class Method:
    def __init__(self, method, rest_api_id, resource_id, uri_function, role_apig_lambda):

        self.__method = method
        self.__rest_api_id = rest_api_id
        self.__resource_id = resource_id
        self.__role_apig_lambda = role_apig_lambda
        uri_fn = 'arn:aws:apigateway:us-east-1:lambda:path/2015-03-31/functions/' + uri_function + '/invocations'
        self.__uri_function = uri_fn

        response = client.put_method(
            restApiId=self.__rest_api_id,
            resourceId=self.__resource_id,
            httpMethod=self.__method,
            authorizationType='NONE',
            apiKeyRequired=False
        )

        response1 = client.put_method_response(
            restApiId=self.__rest_api_id,
            resourceId=self.__resource_id,
            httpMethod=self.__method,
            statusCode='200',
            responseModels={
                'application/json': 'Empty'
            }
        )


        response10 = client.put_integration(
            restApiId=self.__rest_api_id,
            resourceId=self.__resource_id,
            httpMethod=self.__method,
            type='AWS_PROXY',
            integrationHttpMethod='POST',
            #uri='arn:aws:apigateway:us-east-1:lambda:path/2015-03-31/functions/arn:aws:lambda:us-east-1:845002154711:function:clientesGet/invocations',
            uri=self.__uri_function,
            passthroughBehavior='WHEN_NO_MATCH',
            cacheNamespace='ztbweg',
            contentHandling='CONVERT_TO_TEXT',
            timeoutInMillis=29000,
            #credentials='arn:aws:iam::845002154711:role/ROLE-APIG_LAMBDA'
            credentials=self.__role_apig_lambda
        )


        response12 = client.put_integration_response(
            restApiId=self.__rest_api_id,
            resourceId=self.__resource_id,
            httpMethod=self.__method,
            statusCode='200',
            responseTemplates={'application/json': 'None'}
        )


    

        







