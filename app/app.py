from flask import Flask, render_template,request,session,redirect,url_for
from passw import hash_pass
from store import add_user
from forms import RegistrationForm
import os

app = Flask(__name__)
app.secret_key=os.getenv('SK')

@app.route("/home",methods=['POST','GET'])
def index():
    return render_template("homepage.html")

@app.route("/register", methods=['POST','GET'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        print("dfsdf")
    return render_template("registration.html",form=form)

@app.route("/pass", methods=['POST','GET'])
def passs():
    plain_password = request.form.get('pass')
    hashed_password = hash_pass(plain_password)
    username = request.form.get('username')
    add_user(username, hashed_password)
    return ""