import boto3
import json

class Bucket:
    def __init__(self, nome):
        
        self.__nome = nome
        

    def cria_bucket(self):
        
        self.__nome
        client = boto3.client('s3')

        response = client.create_bucket(
            ACL='private',
            Bucket=self.__nome
        )

        s3 = boto3.resource('s3')
        s3.meta.client.upload_file("functions\/todosGet\clientesGet.zip", self.__nome, 'clientesGet.zip') 
        s3.meta.client.upload_file("functions\/todosGet\ordensGet.zip", self.__nome, 'ordensGet.zip') 
        s3.meta.client.upload_file("functions\/todosGet\produtosGet.zip", self.__nome, 'produtosGet.zip') 
        s3.meta.client.upload_file("functions\/umGet\clienteGet.zip", self.__nome, 'clienteGet.zip') 
        s3.meta.client.upload_file("functions\/umGet\ordemGet.zip", self.__nome, 'ordemGet.zip') 
        s3.meta.client.upload_file("functions\/umGet\produtoGet.zip", self.__nome, 'produtoGet.zip')        
        s3.meta.client.upload_file("functions\/umDelete\clienteDelete.zip", self.__nome, 'clienteDelete.zip')
        s3.meta.client.upload_file("functions\/umDelete\produtoDelete.zip", self.__nome, 'produtoDelete.zip')
        s3.meta.client.upload_file("functions\/umDelete\ordemDelete.zip", self.__nome, 'ordemDelete.zip')
        s3.meta.client.upload_file("functions\/umPost\clientePost.zip", self.__nome, 'clientePost.zip')
        s3.meta.client.upload_file("functions\/umPost\produtoPost.zip", self.__nome, 'produtoPost.zip')
        s3.meta.client.upload_file("functions\/umPost\ordemPost.zip", self.__nome, 'ordemPost.zip')
        s3.meta.client.upload_file("functions\/umPatch\clientePatch.zip", self.__nome, 'clientePatch.zip')
        s3.meta.client.upload_file("functions\/umPatch\produtoPatch.zip", self.__nome, 'produtoPatch.zip')
        s3.meta.client.upload_file("functions\/umPatch\ordemPatch.zip", self.__nome, 'ordemPatch.zip')
        

    @property
    def nome(self):
        return self.__nome

             