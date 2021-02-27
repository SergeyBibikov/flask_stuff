import json
from re import L
from flask import Flask,session,request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, login_manager
from flask_debugtoolbar import DebugToolbarExtension
from flask_admin import Admin


db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
toolbar = DebugToolbarExtension()
adminka = Admin(template_mode='bootstrap3')

def create_app():
    app = Flask(__name__)
    app.config.from_envvar("FLASK_CONFIG")

    toolbar.init_app(app)
    db.init_app(app)
    migrate.init_app(app,db)
    login_manager.init_app(app)
    
    from .adminpage import MyAdminIndexView,return_all_views
    adminka.init_app(app,index_view=MyAdminIndexView())

    @app.before_first_request
    def init_admin_page():
        global adminka
        for view in return_all_views(db.session):
            adminka.add_view(view)
    
    @app.before_request
    def init_add_cart():
        cart_cookie = request.cookies.get('cart')
        if cart_cookie:
            cart = json.loads(request.cookies.get('cart'))
            session['cart-size'] = len(cart)
        else:
            session['cart-size'] = 0

    with app.app_context():
        from .views.registration import registration
        from .views.home import home
        from .views.auth import auth
        from .views.manufacturer import manufacturers
        from .views.products import products
        from .views.api import api
        #from .views.admin import admin
        from .views.cart import cart

        app.register_blueprint(registration)
        app.register_blueprint(home)
        app.register_blueprint(auth)
        app.register_blueprint(manufacturers)
        app.register_blueprint(products)
        app.register_blueprint(api)
        #app.register_blueprint(admin)
        app.register_blueprint(cart)

        
        return app



