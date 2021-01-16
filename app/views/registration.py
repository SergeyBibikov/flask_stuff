from flask import Blueprint,render_template,redirect
from .forms import RegistrationForm
from ..models import Users
from .. import db

registration = Blueprint('registration',__name__)

@registration.route("/register", methods=['POST','GET'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        Users.query.all()
        return redirect("login")
    return render_template("registration.html",form=form)