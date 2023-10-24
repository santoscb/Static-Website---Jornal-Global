# Explicando as alterações feitas no index.html

## Script
Foi necessário adicionar um script no index.html para definir a função `callAPI`, a qual vai pegar o nome, email e comentário enviados pelo cliente no website como parâmetros. Também foi preciso criar um Headers Object e adicionar um novo valor a ele com `myHeaders.append`, o qual irá declarar o conteúdo como uma `application/json` - para que a request possa ser interpretada corretamente pelo navegador. A seguir, utilizamos o método `JSON.stringify` para converter os valores obtidos em uma string JSON, e criamos a variável `requestOptinons` que contém um objeto JSON com parâmetros para uma API call. Ao final, é criada a API call com o método `fetch()`, onde é inserida a `Invoke URL` e a variável `requestOptions`.
```
  <script>
      var callAPI = (nome,email,comentario)=>{
          var myHeaders = new Headers();
          myHeaders.append("Content-Type", "application/json");
          var raw = JSON.stringify({"nome":nome,"email":email,"comentario":comentario});
          var requestOptions = {
              method: 'POST',
              headers: myHeaders,
              body: raw,
              redirect: 'follow'
          };
          fetch("https://2l11rb6pba.execute-api.us-east-2.amazonaws.com/Dev", requestOptions)
          .then(response => response.text())
          .then(result => alert(JSON.parse(result).body))
          .catch(error => console.log('error', error));
      }
  </script>
```

## Body

- A imagem com o logo do Banco Carrefour foi removida: `<img src="https://hermes.digitalinnovation.one/companies/2b580e76-3c81-4874-99fd-80ed7fdc62dc.png" alt="Logotipo Banco Carrefour">`.

- A heading tag `<h1>` foi modificada para conter a mensagem `Envier sua opinião`.

- No primeiro input, em `<p class="name">`, foi alterado o placeholder e o id para `nome`.

- No terceiro input, em `<p class="text">` foi modificado o id para `comentario`.

- No elemento `<button type` foi adicionado um evento `onclick` para chamar a função callAPI.

