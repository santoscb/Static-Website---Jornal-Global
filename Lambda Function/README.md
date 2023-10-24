## Explicando a função Lambda

- Criamos um objeto DynamoDB em `dynamodb = boto3.resource('dynamodb')` e o utilizamos para selecionar nossa tabela com `table = dynamodb.Table('JornalGlobal')`
  
- É definida a função handler que o serviço Lambda irá utilizar como entry point:
  ```
  def lambda_handler(event, context):
    name = event['nome']
    email = event['email'] 
    comentario = event['comentario']
    ```
- Para escrever o nome, email e comentário na tabela utilizamos:
  ```
  response = table.put_item(
        Item={
            'Nome': name,
            'Comentario': comentario,
            'ID': email
            })
  ```
     -  O email foi colocado como partition key para que nenhum envio seja reescrito, uma vez que o nome e o comentário podem ser repetidos.

## Conectando a função à tabela DynamoDB

No serviço Lambda temos o menu `configurações`, e dentro dele `permissões`, onde foi possível redirecionar a página para criar uma IAM role. A seguinte policy foi criada para permitir que a função adicione, remova ou pegue itens da tabela, assim como permite scans, queries e updates de itens.
```
{
	"Version": "2012-10-17",
	"Statement": [
		{
			"Sid": "VisualEditor0",
			"Effect": "Allow",
			"Action": [
				"dynamodb:PutItem",
				"dynamodb:DeleteItem",
				"dynamodb:GetItem",
				"dynamodb:Scan",
				"dynamodb:Query",
				"dynamodb:UpdateItem"
			],
			"Resource": "arn:aws:dynamodb:us-east-2:674093522283:table/JornalGlobal"
		}
	]
}
```
