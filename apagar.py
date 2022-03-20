import boto3

client = boto3.client('apigateway')


response = client.get_resources(
    restApiId='zi3dvb5lv9'
)
#response['items'][0]['id']


response1 = client.get_rest_api(
    restApiId='i2esuedeb5'
)

response3 = client.get_rest_apis()

response55 = client.create_rest_api(
    name='loja',
    apiKeySource='HEADER',
    endpointConfiguration={
        'types': [
            'REGIONAL',
        ]
    }
)


response3 = client.get_resource(
    restApiId='syvhr3609h',
    resourceId='jy2n44',
)


response5 = client.create_resource(
    restApiId='i2esuedeb5',
    parentId='mjapi6ojhk',
    pathPart='cliente'
)




response5 = client.get_method(
    restApiId='rkl8v505j8',
    resourceId='ztbweg',
    httpMethod='GET'
)

response6 = client.put_method(
    restApiId='rkl8v505j8',
    resourceId='ztbweg',
    httpMethod='GET',
    authorizationType='NONE',
    apiKeyRequired=False
)


response7 = client.get_method_response(
    restApiId='rkl8v505j8',
    resourceId='ztbweg',
    httpMethod='GET',
    statusCode='200'
)


response8 = client.put_method_response(
    restApiId='rkl8v505j8',
    resourceId='ztbweg',
    httpMethod='GET',
    statusCode='200',
    responseModels={
        'application/json': 'Empty'
    }
)


response9 = client.get_integration(
    restApiId='rkl8v505j8',
    resourceId='ztbweg',
    httpMethod='GET'
)

response10 = client.put_integration(
    restApiId='rkl8v505j8',
    resourceId='ztbweg',
    httpMethod='GET',
    type='AWS_PROXY',
    integrationHttpMethod='POST',
    uri='arn:aws:apigateway:us-east-1:lambda:path/2015-03-31/functions/arn:aws:lambda:us-east-1:845002154711:function:clientesGet/invocations',
    passthroughBehavior='WHEN_NO_MATCH',
    cacheNamespace='ztbweg',
    contentHandling='CONVERT_TO_TEXT',
    timeoutInMillis=29000,
    credentials='arn:aws:iam::845002154711:role/ROLE-APIG_LAMBDA'
)

response11 = client.get_integration_response(
    restApiId='rkl8v505j8',
    resourceId='ztbweg',
    httpMethod='GET',
    statusCode='200'
)

response12 = client.put_integration_response(
    restApiId='rkl8v505j8',
    resourceId='ztbweg',
    httpMethod='GET',
    statusCode='200',
    responseTemplates={'application/json': 'None'}
)




