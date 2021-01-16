import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PERMANENT_SESSION_LIFETIME'] =  int(os.getenv('SESSION_LT'))
app.secret_key=os.getenv('SK')
db = SQLAlchemy(app)

from .views.registration import registration
from .views.home import home
from .views.auth import auth

app.register_blueprint(registration)
app.register_blueprint(home)
app.register_blueprint(auth)

