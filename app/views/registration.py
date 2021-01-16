from flask import Blueprint,render_template,redirect,abort
from .forms import RegistrationForm
from app.utils.passw_hash import hash_pass
from ..models import Users
from .. import db

registration = Blueprint('registration',__name__)

@registration.route("/register", methods=['POST','GET'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pass = hash_pass(form.password.data)
        user = Users(email=form.email.data,username=form.username.data,password=hashed_pass)
        db.session.add(user)
        db.session.commit()
        return redirect("login")
    return render_template("registration.html",form=form)