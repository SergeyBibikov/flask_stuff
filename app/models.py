from datetime import datetime
from functools import partialmethod

from sqlalchemy.orm import backref
from flask_login import UserMixin
from . import db

class User(db.Model,UserMixin):
    __tablename__='users'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    email = db.Column(db.String,nullable=False)
    username = db.Column(db.String,nullable=False)
    password = db.Column(db.String,nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'), nullable=False, default=1)
    def __repr__(self):
        return f"User (id={self.id})"

class Role(db.Model):
    __tablename__='roles'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String,nullable=False)
    user_rel= db.relationship('User',backref='role', lazy='joined')

favourites = db.Table('favourites',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
    db.Column('product_id', db.Integer, db.ForeignKey('products.id'), primary_key=True))

class Country(db.Model):
    __tablename__='countries'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String, nullable=False)
    alpha_2_code = db.Column(db.String, nullable=False)
    alpha_3_code = db.Column(db.String, nullable=False)
    numeric_code = db.Column(db.Integer, nullable=False)
    products_rel=db.relationship('Product',backref='country',lazy="joined")

class Product(db.Model):
    __tablename__='products'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String,nullable=False)
    price = db.Column(db.Float)
    in_stock_qty = db.Column(db.Integer)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'),nullable=False) 
    country_id = db.Column(db.Integer, db.ForeignKey('countries.id'),nullable=False)
    manufacturer_id = db.Column(db.Integer, db.ForeignKey('manufacturers.id'),
        nullable=False)
    cart_stats_rel = db.relationship('StatAddToCart',backref='product')
    order_item_rel = db.relationship('OrderedItem',backref='product')
    

class Category(db.Model):
    __tablename__='categories'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String,nullable=False)
    products_rel=db.relationship('Product',backref='category',lazy="joined")

class Manufacturer(db.Model):
    __tablename__='manufacturers'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String,nullable=False)
    legal_form_id = db.Column(db.Integer,db.ForeignKey('legalforms.id'))
    products_rel=db.relationship('Product',backref='manufacturer',lazy="joined")

class LegalForm(db.Model):
    __tablename__='legalforms'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String)
    legal_forms_rel=db.relationship('Manufacturer',backref='legal_form',lazy="joined")

class StatAddToCart(db.Model):
    __tablename__='stataddtocart'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    quantity = db.Column(db.Integer,nullable=False)
    time_stamp = db.Column(db.DateTime,nullable=False,default=datetime.now())


class Order(db.Model):
    __tablename__='orders'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    creation_time= db.Column(db.DateTime,nullable=False,default=datetime.now())
    is_paid = db.Column(db.Boolean)
    total_sum = db.Column(db.Float)
    payment_sum = db.Column(db.Float)
    payment_time = db.Column(db.DateTime)
    is_cancelled = db.Column(db.Boolean)
    cancellation_time = db.Column(db.DateTime,nullable=False,default=datetime.now())

class OrderedItem(db.Model):
    __tablename__='ordereditems'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    price_on_purchase = db.Column(db.Float,nullable=False)
    quantity = db.Column(db.Integer,nullable=False)


    