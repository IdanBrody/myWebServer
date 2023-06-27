# This file is made to handle the Catalog page.
from Database.MySQL_Connection import connect_to_database
from flask import render_template


def handle_catalog(user_name, category_filter, vendor_filter, gender_filter):
    query = "SELECT * FROM products WHERE 1=1"
    if category_filter:
        query += " AND category = '{}'".format(category_filter)
    if vendor_filter:
        query += " AND vendor = '{}'".format(vendor_filter)
    if gender_filter:
        query += " AND gender = '{}'".format(gender_filter)
    connection = connect_to_database()
    cursor = connection.cursor()
    cursor.execute(query)
    products = cursor.fetchall()
    return render_template('catalog.html', user_name=user_name, products=products, category=category_filter, vendor=vendor_filter, gender=gender_filter)