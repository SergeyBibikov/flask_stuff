from flask import Blueprint, render_template,session,redirect,request
from flask.helpers import url_for
from flask_login import login_user,logout_user
from .forms import LoginForm

auth = Blueprint('auth',__name__)

from ..models import User,Role
from .. import login_manager

@login_manager.user_loader
def load_user(user_id):
    user = User.query.get(user_id)
    return user

@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for('auth.login',next=request.path))

@auth.route("/login",methods=['POST','GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        login_user(user)
        session['role']=user.role.name
        next = request.args.get('next')
        if next:
            return redirect(next)
        else:
            return redirect("home")
    return render_template("login.html",form=form)

@auth.route("/logout")
def logout():
    logout_user()
    return redirect('home')