from flask import Blueprint, render_template,session,redirect
from .forms import LoginForm

auth = Blueprint('auth',__name__)


@auth.route("/login",methods=['POST','GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        session['user']=form.username.data
        return redirect("home")
    return render_template("login.html",form=form)