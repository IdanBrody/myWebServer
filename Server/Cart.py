from flask import session, redirect, url_for


def add_item_to_cart(product_id):
    session['shopping_cart'].append(product_id)
    return redirect(url_for('catalog'))