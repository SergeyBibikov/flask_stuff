import os
from flask import Flask
from flask import request
from flask import make_response
from flask import render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime


app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ(['SK'])
bootstrap = Bootstrap(app)
moment = Moment(app)
@app.route("/")
def index():
    return render_template("index.html",current_time=datetime.utcnow())

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

@app.errorhandler(404)
def not_found(e):
    return render_template("404.html"), 404