## Criação do API gateway

O nome escolhido para o gateway foi `JornalGlobal`, com protocolo REST. Foi utilizado o request method `POST` para integrar com a função Lambda - é necessário inserir a arn da função. A seguir foi habilitado o CORS, que permite que uma aplicação web acesse recursos em um servidor cuja origem é diferente da sua. Por último, foi feito o deploy deste gateway.
