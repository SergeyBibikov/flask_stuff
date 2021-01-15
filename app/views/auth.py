from flask import Blueprint, render_template
from .forms import LoginForm

auth = Blueprint('auth',__name__)


@auth.route("/login",methods=['POST','GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print("Ok")
    return render_template("login.html",form=form)