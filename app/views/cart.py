from flask import Blueprint,render_template,request,make_response,session,redirect,url_for
import json


cart = Blueprint('cart',__name__)

from ..models import Product
from .forms import CartEditItemForm

CART_COOKIE_LIFETIME=604800

@cart.route("/cart",methods=['GET','POST'])
def the_cart():
    global CART_COOKIE_LIFETIME

    form=CartEditItemForm()
    cart_dict_html={}
    cookie_cart = request.cookies.get('cart')

    if cookie_cart:
        cookie_cart = json.loads(cookie_cart)
        for item in cookie_cart.items():
            product = Product.query.get(item[1]["id"])
            quantity=item[1].get("qty",0)
            cart_dict_html[item[0]] = {"product": product,"qty":int(quantity)}

    if form.delete_item.data:
        cookie_cart.pop(f'product_{form.product_id.data}')
        cart_dict_html.pop(f'product_{form.product_id.data}')
        new_cart_cookie = json.dumps(cookie_cart)
        resp = make_response(redirect(url_for('cart.the_cart')))
        resp.set_cookie('cart',new_cart_cookie, max_age=CART_COOKIE_LIFETIME, samesite='Lax')
        return resp

    if form.edit_quantity.data:
        print(request.form.to_dict(flat=False))
        cookie_cart[f'product_{form.product_id.data}']['qty']=form.quantity.data
        cart_dict_html[f'product_{form.product_id.data}']['qty']=form.quantity.data
        new_cart_cookie = json.dumps(cookie_cart)
        resp = make_response(redirect(url_for('cart.the_cart')))
        resp.set_cookie('cart',new_cart_cookie, max_age=CART_COOKIE_LIFETIME, samesite='Lax')
        return resp

    return render_template("cart/cart.html",cart=cart_dict_html,form=form)