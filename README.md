# flask-login
`Repositório onde é estudado a implementação do sistema de login do flask, utilizando a lib flask-login`

## Como Rodar
* __Preparação do banco de dados:__
`Este procedimento deve ser executado primeiro, uma vez que o flask faz consulta ao banco de dados, precisamos garantir que ele exista.`
* para o caso do sistema linux(Debian based):
    - sudo apt install mysql-server libmysqlclient-dev;
    - Durante instalação, será solicitado que crie uma senha para o usuário root, crie alguma senha;
    - Com tudo instalado, o mysql já pode ser acessado rodando:
        - mysql -u root -psenha; `mysql -u usuario(root no caso) -p, e será solicitado a senha`.
    * Criando o banco de dados:
        `O banco de dados deve ser criado anteriormente, as tabelas serão criadas assim que o main.py for executado, com o método db.create_all();`
        - Dentro do mysql, rodar: CREATE DATABASE flask_login;
     
* __Criação do ambiente virtual:__
    - python -m venv .venv; `para criar o ambiente`
    - source .venv/bin/activate; `para ativar o ambiente`

* __Clone do repositório:__
    `Dentro do ambiente virtual previamente criado, rodar`
    - git clone https://github.com/victor-s-santos/flask-login.git;
    - cd flask-login;

* __Instalar as dependências:__
    - pip install -r requirements.txt;

* __Subir o servidor:__
    - python main.py;
