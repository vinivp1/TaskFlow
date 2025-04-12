# API de Tarefas com Flask
Este projeto é uma API simples desenvolvida em Flask, que oferece funcionalidades de cadastro e login de usuários, além do gerenciamento de tarefas. A API permite que os usuários se registrem, façam login e gerenciem suas tarefas com as seguintes operações: criar, editar, excluir e listar tarefas. A autenticação é gerida com **Flask-Login**, utilizando sessões para garantir que apenas usuários autenticados possam acessar as rotas protegidas. O banco de dados é gerenciado pelo **Flask-SQLAlchemy** para armazenar informações de usuários e tarefas de forma persistente.

### Funcionalidades:
* Cadastro e login de usuários com autenticação via sessão (Flask-Login).
* Criação, edição, exclusão e listagem de tarefas.
* Proteção de rotas com autenticação para garantir que somente usuários logados possam acessar e modificar suas tarefas.

### Tecnologias utilizadas:
* **Flask**: Framework Python para criação da API.
* **Flask-Login**: Gerenciamento de sessões e autenticação de usuários.
* **Flask-SQLAlchemy**: ORM utilizado para interação com o banco de dados SQLite.

Este projeto é ideal para aprender sobre a criação de APIs com Flask, autenticação de usuários com sessões e operações CRUD simples em um banco de dados relacional. A API está pronta para ser integrada com front-ends ou utilizada como base para projetos mais complexos.

## Como rodar o projeto:

1. Clone o repositório.
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
3. Configure o banco de dados (criar tabelas):
   ```bash
        python
        from app import db
        db.create_all()
        exit()
4. Inicie o servidor Flask:
    ```bash
        flask run
