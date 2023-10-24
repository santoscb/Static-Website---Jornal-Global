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
     -  O email foi colocado como primary key para que nenhum envio seja reescrito, uma vez que o nome e o comentário podem ser repetidos.
