from os import environ

from lib_ms_api.settings import create_app

db_url = environ.get('DATABASE_URL')
db_url = 'localhost' if db_url is None else db_url

db_port = environ.get('DATABASE_PORT')
db_port = '5432' if db_port is None else db_port

db_user = environ.get('DATABASE_USER') # ms_auth
db_user = 'postgres' if db_user is None else db_user

db_password = environ.get('DATABASE_PASSWORD') # Ms4uth@db
db_password = 'reis' if db_password is None else db_password

[app, db] = create_app(f'postgresql://{db_user}:{db_password}@{db_url}:{db_port}/ms_auth', True, True)

app.config['SECRET_KEY'] = 'secretProfReisClass'
app.config['ALGORITHM'] = 'HS256'
