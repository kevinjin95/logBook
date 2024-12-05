from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/jk1234/Documents/perso/logBook/logBook/instance/database.db'
db = SQLAlchemy(app)
app.app_context().push()
app.config['SECRET_KEY'] = '44d9de2b82a1deb9057de798'
bcrypt = Bcrypt(app)
loginManager = LoginManager(app)

from logBook import routes
