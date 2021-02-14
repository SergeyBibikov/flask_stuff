from app.models import Role
from flask import Blueprint,render_template,current_app,session,request
from itsdangerous import Serializer

home = Blueprint('home',__name__)

@home.route("/home",methods=['GET'])
@home.route("/",methods=['GET'])
def index():
    serializer = Serializer(current_app.config.get('SECRET_KEY'))
    cart_cookie = request.cookies.get('cart')
    if cart_cookie:
        cart = serializer.loads(request.cookies.get('cart'))
        session['cart-size'] = len(cart)
    else:
        session['cart-size'] = 0
    return render_template("homepage.html")

@home.route("/populate")
def populate():
    from .. import db
    db.create_all()
    db.session.commit()
    return "Ok"