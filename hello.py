from flask import Flask
from flask import request
from flask import make_response

app = Flask(__name__)

@app.route("/<name>")
def hello(name):
    resp = make_response(f"Hello {name}")
    resp.set_cookie("a cookie","a cookie value")
    if name == "John":
        return "I don't know any Johns", 400
    return resp