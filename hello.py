from flask import Flask
from flask import request
from flask import make_response
from flask import render_template


app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/<name>")
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