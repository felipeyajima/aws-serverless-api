from lambda1 import Function
from dynamodb import Dynamodb
from policy_Dynamo import Policy_Dynamo
from role import Role
from policy_Lambda import Policy_Lambda
from role_APIGateway_Lambda import Role_APIGateway_Lambda
from s3 import Bucket
from apigateway import Rest
from apigateway import Resource
from apigateway import Method

dynamodb = Dynamodb('loja1','')
dynamodb.cria_tabela()
dynamodb.popula_tabela()
#dynamodb.cria_gsi()
dynamodb.cria_gsi2()


#============= permissionamento IAM ==============
#Cria uma policy de acesso à tabela do DynamoDB
policy = Policy_Dynamo('POLICY-ACESSO_AO_DYNAMO1', dynamodb.nome, dynamodb.arn, '')

#Cria uma policy que permite acesso ao Lambda
policy1 = Policy_Lambda('POLICY-ACESSO_AO_LAMBDA1', '')

# cria a Role e atacha a policy dy dynamodb para o Lambda acessar
role = Role('ROLE-LAMBDA_DYNAMO1', policy.arn, '')

#cria uma role e atacha a policy de acesso ao lambda para o API Gateway acessar
roleAPIG_Lambda = Role_APIGateway_Lambda('ROLE-APIG_LAMBDA1', policy1.arn, '')


bucketlambda = Bucket('yajima-linuxacademy-202007111')
bucketlambda.cria_bucket()

#Criando as funcões e importando o código do S3 
clientes_get = Function('clientes', 'Get', bucketlambda.nome, role.arn, '')
ordens_get = Function('ordens', 'Get', bucketlambda.nome, role.arn, '')
produtos_get = Function('produtos', 'Get', bucketlambda.nome, role.arn, '')

cliente_get = Function('cliente', 'Get', bucketlambda.nome, role.arn, '')
ordem_get = Function('ordem', 'Get', bucketlambda.nome, role.arn, '')
produto_get = Function('produto', 'Get', bucketlambda.nome, role.arn, '')

cliente_post = Function('cliente', 'Post', bucketlambda.nome, role.arn, '')
ordem_post = Function('ordem', 'Post', bucketlambda.nome, role.arn, '')
produto_post = Function('produto', 'Post', bucketlambda.nome, role.arn, '')

cliente_patch = Function('cliente', 'Patch', bucketlambda.nome, role.arn, '')
ordem_patch = Function('ordem', 'Patch', bucketlambda.nome, role.arn, '')
produto_patch = Function('produto', 'Patch', bucketlambda.nome, role.arn, '')

cliente_delete = Function('cliente', 'Delete', bucketlambda.nome, role.arn, '')
ordem_delete = Function('ordem', 'Delete', bucketlambda.nome, role.arn, '')
produto_delete = Function('produto', 'Delete', bucketlambda.nome, role.arn, '')


rest = Rest('loja1', '', '')
r_cliente = Resource('cliente', rest.id, rest.barra, '')
api_clientes_get = Method('GET', rest.id, r_cliente.resource_id, clientes_get.arn, roleAPIG_Lambda.arn)
#api_clientes_get = Method('GET', rest.id, r_cliente.resource_id, 'arn:aws:lambda:us-east-1:921728388910:function:clientesGet', 'arn:aws:iam::921728388910:role/ROLE-APIG_LAMBDA')

r_produto = Resource('produto', rest.id, rest.barra, '')
api_produtos_get = Method('GET', rest.id, r_produto.resource_id, produtos_get.arn, roleAPIG_Lambda.arn)
#api_produtos_get = Method('GET', rest.id, r_produto.resource_id, 'arn:aws:lambda:us-east-1:921728388910:function:produtosGet', 'arn:aws:iam::921728388910:role/ROLE-APIG_LAMBDA')

r_ordem = Resource('ordem', rest.id, rest.barra, '')
api_ordens_get = Method('GET', rest.id, r_ordem.resource_id, ordens_get.arn, roleAPIG_Lambda.arn)
#api_ordens_get = Method('GET', rest.id, r_ordem.resource_id, 'arn:aws:lambda:us-east-1:921728388910:function:ordensGet', 'arn:aws:iam::921728388910:role/ROLE-APIG_LAMBDA')









