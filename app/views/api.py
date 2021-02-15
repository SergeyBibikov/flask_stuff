from flask import Blueprint,current_app
from flask import Flask,render_template,request,redirect,make_response,flash,jsonify
import json

api = Blueprint('api',__name__)
CART_COOKIE_LIFETIME =604800

@api.route('/addtocart', methods=['POST'])
def add_to_cart():
    global CART_COOKIE_LIFETIME
    added_object = request.get_json()
    added_product = added_object.get('product')
    added_qty = added_object.get('qty')
    current_cart = request.cookies.get('cart')

    if not current_cart:
        cart_cookie = json.dumps({f'product_{added_product}':{"id":added_product,"qty":added_qty}})
        resp = make_response(json.dumps({"success":"The product was added to cart"}))
        resp.set_cookie('cart', cart_cookie, max_age=CART_COOKIE_LIFETIME, samesite='Lax')
        return resp

    cart_in_cookies = json.loads(current_cart) 

    if f'product_{added_product}' in cart_in_cookies:
        resp = make_response(json.dumps({"success":"The product was altered"}))
    else:
        resp = make_response(json.dumps({"success":"The product was added to cart"}))
        
    cart_in_cookies[f'product_{added_product}'] = {"id":added_product,"qty":added_qty}
    new_cookie = json.dumps(cart_in_cookies)
    resp.set_cookie('cart', new_cookie, max_age=CART_COOKIE_LIFETIME, samesite='Lax')
    return resp 
