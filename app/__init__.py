import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, login_manager
from flask_debugtoolbar import DebugToolbarExtension

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
toolbar = DebugToolbarExtension()

def create_app():
    app = Flask(__name__)
    app.config.from_envvar("FLASK_CONFIG")

    toolbar.init_app(app)
    db.init_app(app)
    migrate.init_app(app,db)
    login_manager.init_app(app)

    with app.app_context():
        from .views.registration import registration
        from .views.home import home
        from .views.auth import auth
        from .views.manufacturer import manufacturers
        from .views.products import products

        app.register_blueprint(registration)
        app.register_blueprint(home)
        app.register_blueprint(auth)
        app.register_blueprint(manufacturers)
        app.register_blueprint(products)

        return app



