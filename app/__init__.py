from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:senha@localhost/flask_login'
app.config['SECRET_KEY'] = 'segredo'
login_manager = LoginManager(app)
db = SQLAlchemy(app)

