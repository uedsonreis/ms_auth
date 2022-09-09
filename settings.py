from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cli import FlaskCLI
from flask_migrate import Migrate, command

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:reis@localhost:5432/ms_auth'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['DEBUG'] = True


db = SQLAlchemy(app)


migrate = Migrate(app, db)
FlaskCLI(app)
