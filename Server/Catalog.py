# This file is made to handle the Catalog page.

from Database.MySQL_Connection import connect_to_database
from flask import render_template
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

def handle_catalog(user_name):
    connection = connect_to_database()
    cursor = connection.cursor()
    query = "SELECT product_link FROM products"
    cursor.execute(query)
    products = cursor.fetchall()
    return render_template('catalog.html', user_name=user_name, products=products)