import os
from flask import Flask,request,make_response,render_template
from flask import redirect,session,url_for,flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired
from datetime import datetime


app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SK')
bootstrap = Bootstrap(app)
moment = Moment(app)

class NameForm(FlaskForm):
    name = StringField("What's your name?",validators=[DataRequired(message="Enter you name, please")])
    submit = SubmitField("Submit")

@app.route("/",methods = ["GET","POST"])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name!=form.name.data:
            flash(f"Name changed from {old_name} to {form.name.data}")
        session['name'] = form.name.data
        return redirect(url_for("index"))
    return render_template("index.html", form=form, name=session.get('name'), current_time=datetime.utcnow())

@app.route("/user/<name>")
def name(name):
    if name == "John":
        return "I don't know any Johns", 400
    return render_template("user.html",name=name)

@app.route("/list")
def list():
    f_list = ["One","Two","Three"]
    return render_template("list.html",list=f_list)

@app.route("/sub")
def sub():
    return render_template("subbase.html")

@app.route("/clear")
def clear():
    print(help(session))
    session['name'] = None
    return redirect(url_for("index"))

@app.errorhandler(404)
def not_found(e):
    return render_template("404.html"), 404