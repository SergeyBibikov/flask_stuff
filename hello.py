import os
from flask import Flask,request,make_response,render_template
from flask import redirect,session,url_for,flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SK')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
bootstrap = Bootstrap(app)
moment = Moment(app)
db = SQLAlchemy(app)

class NameForm(FlaskForm):
    name = StringField("What's your name?",validators=[DataRequired(message="Enter you name, please")])
    submit = SubmitField("Submit")

class Role(db.Model):
    __tablename__='roles'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(64),unique=True)
    users = db.relationship('User', backref='role',lazy='dynamic')
    
    def __repr__(self):
        return '<Role %r>' % self.name
        
class User(db.Model):
    __tablename__='users'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    def __repr__(self):
        return '<User %r>' % self.username

@app.route("/",methods = ["GET","POST"])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            db.session.commit()
            session['known'] = False
            flash("New User added")
        else:
            session['known'] = True
        session['name'] = form.name.data
        return redirect(url_for("index"))
    return render_template("index.html",
                             form=form,
                             name=session.get('name'),
                             known=session.get('known', False),
                             current_time=datetime.utcnow())

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
    session['name'] = None
    return redirect(url_for("index"))

@app.errorhandler(404)
def not_found(e):
    return render_template("404.html"), 404

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Role=Role)