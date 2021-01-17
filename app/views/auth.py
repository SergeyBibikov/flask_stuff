from flask import Blueprint, render_template,session,redirect
from .forms import LoginForm

auth = Blueprint('auth',__name__)

from ..models import User,Role

@auth.route("/login",methods=['POST','GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        session['user']= username
        session['role']=Role.query.filter_by(id=User.query.filter_by(username=username).first().role_id).first().name
        print(f"The user {session.get('user')} has successfully logged in!")
        return redirect("home")
    return render_template("login.html",form=form)

@auth.route("/logout")
def logout():
    session.clear()
    return redirect('home')