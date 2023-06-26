from flask import session, redirect, url_for, request


def add_item_to_cart(product_id):
    if 'Shopping_Cart' not in session:
        session['Shopping_Cart'] = []
    session['Shopping_Cart'].append(product_id)
    print("shopping cart: ", session['Shopping_Cart'])
    return "Product added successfully"
