import json
import boto3
from time import gmtime, strftime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('JornalGlobal')
now = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())

def lambda_handler(event, context):
    name = event['nome']
    email = event['email'] 
    comentario = event['comentario']
    response = table.put_item(
        Item={
            'Nome': name,
            'Comentario': comentario,
            'ID': email
            })
    return {
    'statusCode': 200,
    'body': json.dumps('Obrigado pela sua opiniao')
    }
