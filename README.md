
# Desafio Estagiario JR FullStack

Este repositorio contem a parte Back-End da aplicação que se encontra aqui: [FRONT](github.com/DiogoPedrosaa/EstagiarioJR-FullStack-Challenge-Front), Ao utilizar a API certifique-se de que o CORS no arquivo settings esta compativel com o endereço que está sendo executado a aplicação do front-end.

Seria uma boa pratica subir o repositorio com um gitignore configurado para não expor arquivos sensiveis da aplicação, mas para a praticidade na realização de testes no projeto preferi manter sem o ignore.





## Tecnologias utilizadas

- **Django com Django Rest Framework**
- **Autenticação JWT**: Para garantir uma maior segurança na API, fornecendo um token no login, necessario para realizar algumas requisições
- **Swagger**: Utilizado para documentar todos os endpoints disponiveis na API, assim como os dados que esperam receber.
- **Python-Decouple**: Para proteger dados sensiveis da aplicação como Secret Keys ou ate mesmo dados do banco.




## Rodando localmente

Clone o projeto

```bash
  git clone https://github.com/DiogoPedrosaa/EstagiarioJR-FullStack-Challenge
```

Crie um ambiente virtual na raiz do projeto

```bash
python -m venv venv
source venv/bin/activate  # No Windows, use venv\Scripts\activate
```

Instale as dependências

```bash
  pip install -r requirements.txt
```

Configure as variáveis de ambiente: Renomeie o arquivo .env.example para .env e ajuste as configurações conforme necessário.

Execute as migrações do banco de dados:

```bash
  python manage.py migrate
```

Inicie o servidor (preferencia na porta 80 já que o front está configurado para consumir os dados dessa porta.)

```bash
  python manage.py runserver localhost:80
```




