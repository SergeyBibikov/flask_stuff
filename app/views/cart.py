from flask import Blueprint,render_template,request,make_response,session,redirect,url_for
import json


cart = Blueprint('cart',__name__)

from ..models import Product
from .forms import CartEditItemForm

CART_COOKIE_LIFETIME=604800

@cart.route("/cart",methods=['GET','POST'])
def the_cart():
    global cart_cookie_lifetime

    form=CartEditItemForm()
    cart=[]
    cookie_cart = request.cookies.get('cart')

    if cookie_cart:
        cookie_cart = json.loads(cookie_cart)
        for item in cookie_cart.items():
            product = Product.query.get(item[1]["id"])
            quantity=item[1].get("qty",0)
            cart.append({"product": product,"qty":quantity})

    # if form.delete_item.data:
    #         item_to_delete={"product":Product.query.get(form.product_id.data),
    #                         "qty":form.current_qty}
    #         print(item_to_delete)
    #         cart.remove(item_to_delete)
    #         cart_for_cookies = []
    #         cart_for_html = cart
    #         for item in cart:
    #             cart_for_cookies.append({"product":item["product"].id,"qty":item["qty"]})
    #         new_cart_cookie = json.dumps(cart_for_cookies)
    #         if len(cart_for_cookies)==0:
    #             resp = make_response(render_template("cart/cart.html",cart=[],form=form))
    #             resp.delete_cookie('cart')
    #             return resp
    #         else:
    #             resp = make_response(render_template("cart/cart.html",cart=cart_for_html,form=form))
    #             resp.set_cookie('cart',new_cart_cookie, max_age=CART_COOKIE_LIFETIME, samesite='Lax')
    #             return resp
    return render_template("cart/cart.html",cart=cart,form=form)