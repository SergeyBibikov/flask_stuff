from flask import Blueprint, render_template,flash,redirect,url_for
from flask_login import login_required
from .forms import ProductSearchForm
from ..utils.helpers import is_admin

from sqlalchemy import func

products = Blueprint('products',__name__)
from ..models import Product
from .. import db

@products.route("/products/add")
@login_required
@is_admin
def add_product():
    pass

@products.route("/products/edit")
@login_required
@is_admin
def edit_product(search_form):
    
    pass

@products.route("/products/find", methods=['GET','POST'])
def find_product():
    products_list=[]
    search_form = ProductSearchForm()
    if search_form.name.data:
        products_list = product_search(search_form)
    return render_template('products/products_list.html',search_form=search_form,products_list=products_list)

def product_search(search_form):
    search_string = search_form.name.data.lower()
    if search_form.search_filter.data=='Начинается с':
        search_term=f'{search_string}%'
    elif search_form.search_filter.data=='Содержит':
        search_term=f'%{search_string}%'
    elif search_form.search_filter.data=='Заканчивается на':
        search_term=f'%{search_string}'
    elif search_form.search_filter.data=='Полностью совпадает с':
        search_term=search_string
    products_list = Product.query.filter(func.lower(Product.name).like(search_term)).order_by(Product.name).all()
    return products_list