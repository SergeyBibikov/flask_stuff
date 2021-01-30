from sqlalchemy.orm import backref
from . import db

class User(db.Model):
    __tablename__='users'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    email = db.Column(db.String,nullable=False)
    username = db.Column(db.String,nullable=False)
    password = db.Column(db.String,nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'), nullable=False, default=1)

class Role(db.Model):
    __tablename__='roles'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String,nullable=False)
    user_rel= db.relationship('User',backref='role')

favourites = db.Table('favourites',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
    db.Column('product_id', db.Integer, db.ForeignKey('products.id'), primary_key=True))

class Product(db.Model):
    __tablename__='products'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String,nullable=False)
    country_of_origin = db.Column(db.String)
    manufacturer_id = db.Column(db.Integer, db.ForeignKey('manufacturers.id'),
        nullable=False)

class Manufacturer(db.Model):
    __tablename__='manufacturers'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String,nullable=False)
    legal_form_id = db.Column(db.Integer,db.ForeignKey('legalforms.id'))
    products_rel=db.relationship('Product',backref='manufacturer',lazy="dynamic")

class LegalForm(db.Model):
    __tablename__='legalforms'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String)
    legal_forms_rel=db.relationship('Manufacturer',backref='legal_form',lazy="dynamic")