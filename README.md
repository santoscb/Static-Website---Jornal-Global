# Static Website - Jornal Global
Vamos como criar um website estático para que leitores de um jornal enviem suas opiniões. O site irá pedir o nome, email e o comentário do leitor. Para isso, iremos usar o serviço de Cloud Computing AWS. Os arquivos utilizados como referência para o frontend foram retirador do projeto [banco-carrefour-techday-cloud-devops](https://github.com/digitalinnovationone/banco-carrefour-techday-cloud-devops) e modificados de acordo com as necessidades que se apresentaram ao longo do projeto. Para que o website ficasse disponível foi utilizado um bucket S3. Foi criada uma função Lambda para retornar uma mensagem após o envio dos dados pelo cliente, mas principalmente para salvar os dados inputados em uma tabela DynamoDB. Para fazer a conexão entre o bucket S3 e a função Lambda foi necessário criar um API gateway. Por fim, algumas roles IAM foram essenciais para que os serviços tenham permissão para interagir entre si.

![image](https://github.com/santoscb/Static-Website---Jornal-Global/assets/104686090/7f3d126b-6151-4f57-8828-e6a09394149c)


##Estrutura final do projeto
