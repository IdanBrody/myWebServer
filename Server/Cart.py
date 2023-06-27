from flask import session, redirect, url_for, request, render_template
from Database.MySQL_Connection import connect_to_database
import json


def add_item_to_cart(product_id):
    if 'Shopping_Cart' not in session:
        session['Shopping_Cart'] = '[]'
    connection = connect_to_database()
    cursor = connection.cursor()
    query = "SELECT * FROM products WHERE id = {}".format(product_id)
    cursor.execute(query)
    shopping_cart = json.loads(session.get('Shopping_Cart'))
    shopping_cart.append(cursor.fetchone())
    session['Shopping_Cart'] = json.dumps(shopping_cart)
    print("shopping cart: ", session['Shopping_Cart'])
    return "Product added successfully"

def checkout():
    total_price = 0
    if 'Shopping_Cart' not in session:
        session['Shopping_Cart'] = '[]'
    products = json.loads(session.get("Shopping_Cart"))
    for product in products:
        print(product[5])
        total_price += product[5]
    print("products: ", products)
    return render_template('cart.html', products=products, user_name=session.get("user_name", "Guest"), total_price=total_price)