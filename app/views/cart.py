from flask import Blueprint,render_template,request
import json

cart = Blueprint('cart',__name__)

from ..models import Product
from .forms import CartEditItemForm

@cart.route("/cart",methods=['GET','POST'])
def the_cart():
    form=CartEditItemForm()
    cart=[]
    cookie_cart = request.cookies.get('cart')
    if cookie_cart:
        cookie_cart = json.loads(request.cookies.get('cart'))
        for item in cookie_cart:
            product = Product.query.get(item["product"])
            quantity=item["qty"]
            cart.append((product,quantity))
    if form.validate_on_submit():
        if form.quantity>form.stock_qty:
            form.quantity.errors.append("Такого количества нет в наличии")
        if form.delete_item.data:
            cart = [i for i in cart if i[0].name != form.product_id]
    return render_template("cart/cart.html",cart=cart,form=form)