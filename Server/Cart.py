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
    return "Product added successfully"


def remove_item_from_cart(product_id):
    shopping_cart = list(json.loads(session.get('Shopping_Cart')))
    print(product_id)
    print(shopping_cart, "\n")

    items_to_remove = []
    for product in shopping_cart:
        if str(product[0]) == str(product_id):
            items_to_remove.append(product)

    for item in items_to_remove:
        shopping_cart.remove(item)
    session['Shopping_Cart'] = json.dumps(shopping_cart)
    print(json.loads(session.get('Shopping_Cart')), "modified")
    return "Product removed successfully"


def calculate_total_price(products):
    total_price = 0
    for product in products:
        total_price += product[5]
    return total_price


def get_products_from_cart():
    products = json.loads(session.get("Shopping_Cart"))
    return products


def checkout():
    if 'Shopping_Cart' not in session:
        session['Shopping_Cart'] = '[]'
    products = json.loads(session.get("Shopping_Cart"))
    total_price = calculate_total_price(products)
    return render_template('cart.html', products=products, user_name=session.get("user_name", "Guest"), total_price=total_price)


