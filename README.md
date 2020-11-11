# e-dce

### Sistema de votação para Diretório Central dos Estudantes da FAFIC

Essa é uma versão alternativa e melhorada (em todos os sentidos) de sua versão física: [Votação do DCE](https://fescfafic.edu.br/votacao-do-dce/) e [Urna Eletrônica – Django e Raspberry Pi 3B+](https://erlonbcc.wordpress.com/2020/02/02/urna-eletronica-django-e-raspberry-pi-3bplus/)

Desenvolvido usando apenas Django, com configurações de segurança para garantir uma confiabilidade melhor ao sistema.

### Configuração:

Requisitos -> dev:
* Python 3.6+ (Recomendação usar o Python 3.8+)

Você precisa criar um arquivo .env de acordo com o que é configurado no ***settings.py***, comente as configurações da AWS caso não deseje usar.

Se tiver enteresse em usar postgress em desenvolvimento ou fazer deploy com ele em outro lugar, configure dessa forma:

( Deploy ) Recomendação - configurando o PostgreSQL (mude nome do banco, nome do usuário e senha):
```
sudo -i -u postgres psql
CREATE DATABASE nome_do_banco;
CREATE USER nome_usuario WITH PASSWORD 'sua_senha';
ALTER ROLE nome_usuario SET client_encoding TO 'utf8';
ALTER ROLE nome_usuario SET default_transaction_isolation TO 'read committed';
ALTER ROLE nome_usuario SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE nome_do_banco TO nome_usuario;
```

Agora você precisa clonar o repositório

```
git clone https://github.com/ejrgeek/e-dce.git
```

Depois caso queira, pode criar um novo ambiente virtual para rodar a aplicação, você pode ler aqui para saber mais caso não tenha conhecimento sobre: https://pythonacademy.com.br/blog/python-e-virtualenv-como-programar-em-ambientes-virtuais

Depois de criado, você entra no ambiente e roda os comandos

```
pip install -r requirements.txt
```

Pronto, agora rode os comandos:

```
python manage.py migrate
```

Para fazer a migração das tabelas do banco de dados baseados nos Models do Django gerado pelo ORM. Depois você pode rodar o comando para criar um super usuario:
```
python manage.py createsuperuser
```
Depois você pode rodar um:
```
python manage.py runserver
```

A aplicação está no ar (localmente pelo menos rs). Ainda é necessário algumas configurações.
