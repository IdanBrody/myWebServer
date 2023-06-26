from flask import session, redirect, url_for, request, render_template
from Database.MySQL_Connection import connect_to_database


def add_item_to_cart(product_id):
    if 'Shopping_Cart' not in session:
        session['Shopping_Cart'] = []
    connection = connect_to_database()
    cursor= connection.cursor()
    query = "SELECT * FROM products WHERE id = {}".format(product_id)
    cursor.execute(query)
    session['Shopping_Cart'].append(cursor.fetchone())
    print("shopping cart: ", session['Shopping_Cart'])
    return "Product added successfully"

def checkout():
    if 'Shopping_Cart' not in session:
        session['Shopping_Cart'] = []
    products = session.get("Shopping_Cart")
    print("products: ", products)
    return render_template('cart.html', products=products, user_name=session.get("user_name", "Guest"))