from flask import Blueprint,current_app
from flask import Flask,render_template,request,redirect,make_response,flash,jsonify
import json

api = Blueprint('api',__name__)
cart_cookie_lifetime=604800

@api.route('/addtocart', methods=['POST'])
def add_to_cart():
    global cart_cookie_lifetime
    added_object = request.get_json()
    added_product = added_object.get("product")
    current_cart=request.cookies.get('cart')
    if not current_cart:
        cart_cookie = json.dumps([added_object])
        resp = make_response(json.dumps({"success":"The product was added to cart"}))
        resp.set_cookie('cart', cart_cookie, max_age=cart_cookie_lifetime, samesite='Lax')
        return resp
    cart_in_cookies = json.loads(current_cart)    
    if is_product_present(cart_in_cookies,added_product):
        return  make_response(json.dumps({"error":"The product is already in the cart"}),409)
    cart_in_cookies.append(added_object)
    new_cookie = json.dumps(cart_in_cookies)
    resp = make_response(json.dumps({"success":"The product was added to cart"}))
    resp.set_cookie('cart', new_cookie, max_age=cart_cookie_lifetime, samesite='Lax')
    return resp



def is_product_present(cart,pr_id):
    for d in cart:
        if d.get('product') == pr_id:
            return True
    return False