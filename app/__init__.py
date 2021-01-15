import os
from flask import Flask
from .views.registration import registration
from .views.home import home
from .views.auth import auth
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI=')
app.secret_key=os.getenv('SK')
app.register_blueprint(registration)
app.register_blueprint(home)
app.register_blueprint(auth)

db = SQLAlchemy(app)
