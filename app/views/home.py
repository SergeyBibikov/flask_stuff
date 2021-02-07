from app.models import Role
from flask import Blueprint,render_template

home = Blueprint('home',__name__)

@home.route("/home",methods=['GET'])
@home.route("/",methods=['GET'])
def index():
    return render_template("homepage.html")

@home.route("/populate")
def populate():
    from .. import db
    db.create_all()
    db.session.commit()
    return "Ok"