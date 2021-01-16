from . import db

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    email = db.Column(db.String,nullable=False)
    username = db.Column(db.String,nullable=False)
    password = db.Column(db.String,nullable=False)

