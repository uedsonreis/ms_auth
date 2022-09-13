from lib_ms_api.settings import create_app

[app, db] = create_app('postgresql://postgres:reis@localhost:5432/ms_auth', True, True)

app.config['SECRET_KEY'] = 'secretProfReisClass'
app.config['ALGORITHM'] = 'HS256'
