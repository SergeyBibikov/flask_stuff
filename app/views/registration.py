from flask import Blueprint,render_template,redirect
from .forms import RegistrationForm
#from ..models import User

registration = Blueprint('registration',__name__)

@registration.route("/register", methods=['POST','GET'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        #check everything
        return redirect("login")
    return render_template("registration.html",form=form)