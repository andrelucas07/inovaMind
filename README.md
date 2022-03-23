## Descrição do desafioPrecisamos que você desenvolva uma API REST que consuma um serviço (https://jsonplaceholder.typicode.com/todos) e nos retorne uma lista com os 5 primeiros resultados.

Esperamos que você termine esse código em até 3 dias e faça a entrega do mesmo até sexta-feira (21/03), através de um repositório público no Github/Gitlab.
Caso tenha alguma dúvida ou sugestão, fique a vontade para entrar em contato.

## O que nós iremos avaliar?
  - Separação de contextos;
  - Error handing;
  - Manutenabilidade;
  - Baixo acoplamento;
  - Código pythonico;
  - README com todas as instruções de como executar o projeto e como usar os endpoints existentes.


O retorno com sucesso deve ser um JSON no formato:
```json
{
  "id": <id do registro>,
  "title": <nome do registro>,
}
```

O retorno com erro deve ser um JSON no formato:
```json
{
  "error": {
    "reason": "error description",
  }

}
```

## Toda e qualquer consulta na sua API deve gerar um log que deve conter as seguintes

informações:
  - timestamp;
  - retorno raw da API consultada;
  - HTTP status code da API consultada;


## Tecnologias:
  - Linguagem: Python 3;
  - Framework: Flask;
  - Gerenciador de dependências: poetry ou pip (requirements.txt);
  - Você pode usar outras tecnologias/libs que deixem sua implementação flexível, apenas fique atento para o prazo.


## Extras:
Os itens nesta sessão não são obrigatórios, porém contarão como pontos extras:
  - Utilizar algum tipo de autorização na sua API (Ex.: Bearer, Basic Auth, X-API-Key).;
  - Parametrizar a quantidade de itens que serão retornados.;
  - Dockerize sua solução, mas não publique sua imagem. Basta criar um diretório docker na raiz do projeto e colocar qualquer arquivo relacionado dentro dele;
  - Seguir o 12factor app (https://12factor.net/pt_br/);
  - Testes e cobertura;
  - Collection do postman com alguns exemplos de respostas possíveis.

###########################################################################################

## Como rodar esse projeto

```sh
export FLASK_APP=api\\app.py
export FLASK_ENV=Development
export FLASK_DEBUG=True

flask run
```

## Fazendo requisições no postman

'''
**No diretório: "request_postman"**

1 - Acessar o arquivo inovaMind.postman
2 - Copiar todo o conteudo

**No postman:**

1 - Clicar em "Import"
2 - Escolher a opção Raw Text
3 - Colar todo conteudo que foi copiado do arquivo inovaMind.postman
4 - Clica em Continue
5 - Import

**Requisitos para fazer a request**

1 - Em authorization >> type: Escoolher a opção "Basic Auth"
2 - Inserir o login: admin e senha: admin
3 - Clicar em Send
'''
