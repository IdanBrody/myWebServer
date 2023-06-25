# This file is made to handle the Catalog page.
from Database.MySQL_Connection import connect_to_database
from flask import render_template


def handle_catalog(user_name, category_filter=None, vendor_filter=None, gender_filter=None):
    conditions = []
    if category_filter is not None:
        conditions.append("category={}".format(category_filter))
    if vendor_filter is not None:
        conditions.append("vendor={}".format(vendor_filter))
    if gender_filter is not None:
        conditions.append("gender={}".format(gender_filter))
    query = "SELECT product_link FROM products"
    if conditions:
        query += " WHERE" + " AND".join(conditions)
    connection = connect_to_database()
    cursor = connection.cursor()
    cursor.execute(query)
    products = cursor.fetchall()
    return render_template('catalog.html', user_name=user_name, products=products)