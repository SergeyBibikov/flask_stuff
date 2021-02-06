from flask import Blueprint, render_template,session,redirect
from flask_login import login_user,logout_user
from .forms import LoginForm

auth = Blueprint('auth',__name__)

from ..models import User,Role
from .. import login_manager

@login_manager.user_loader
def load_user(user_id):
    user = User.query.get(user_id)
    return user

@auth.route("/login",methods=['POST','GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        #session['user']= username
        login_user(user)
        session['role']=user.role.name
        print(f"The user {session.get('user')} has successfully logged in!")
        return redirect("home")
    return render_template("login.html",form=form)

@auth.route("/logout")
def logout():
    logout_user()
    return redirect('home')