import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, login_manager
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PERMANENT_SESSION_LIFETIME'] =  int(os.getenv('SESSION_LT'))
app.secret_key=os.getenv('SK')
toolbar = DebugToolbarExtension(app)
app.config['DEBUG_TB_TEMPLATE_EDITOR_ENABLED'] = True
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager()
login_manager.init_app(app)

from .views.registration import registration
from .views.home import home
from .views.auth import auth
from .views.manufacturer import manufacturers

app.register_blueprint(registration)
app.register_blueprint(home)
app.register_blueprint(auth)
app.register_blueprint(manufacturers)

