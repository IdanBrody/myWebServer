import json

from flask import Flask, render_template, request, session, redirect, url_for
from Server.Login_SignUp import handle_sign_up, handle_login
from Server.Cart import add_item_to_cart, checkout, remove_item_from_cart, calculate_total_price, get_products_from_cart
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from Catalog import handle_catalog
import os

secret_key = os.urandom(32)
app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = secret_key
jwt = JWTManager(app)
app.secret_key = secret_key


# Route for Home

@app.route("/index")
@app.route('/')
def index():
    user_name = session.get("user_name", "Guest")
    # Render the index.html template
    return render_template('index.html', user_name=user_name)


# Route for login
@app.route('/login', methods=['GET', 'POST'])
def login():
    user_name = session.get("user_name", "Guest")
    if request.method == 'GET':
        return render_template('login.html', user_name=user_name)
    elif request.method == 'POST':
        return handle_login()


# Route for sign up
@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'GET':
        return render_template('sign_up.html')
    elif request.method == 'POST':
        return handle_sign_up()


# Route for catalog
@app.route('/catalog', methods=['GET'])
def catalog():
    user_name = session.get("user_name", "Guest")

    # Get the filters from the request
    category_filter = request.args.get('category')
    vendor_filter = request.args.get('vendor')
    gender_filter = request.args.get('gender')
    return handle_catalog(user_name, category_filter, vendor_filter, gender_filter)


@app.route('/contact', methods=['GET'])
def contact():
    user_name = session.get("user_name", "Guest")
    return render_template('contact.html', user_name=user_name)


@app.route('/logout')
def logout():
    session.clear()  # Clear the session data
    return redirect(url_for('index'))


@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    if session.get('logged_in'):
        product_id = request.form.get('product_id')
        return add_item_to_cart(product_id)
    else:
        return "You must be logged in order to add product to cart"


@app.route('/remove_from_cart', methods=['POST'])
def remove_from_cart():
    if session.get('logged_in'):
        product_id = request.form.get('product_id')
        remove_item_from_cart(product_id)
        return "Product removed successfully"
    else:
        return "You must be logged in order to remove a product from the cart"


@app.route('/Cart', methods=["GET"])
def show_cart():
    return checkout()


if __name__ == '__main__':
    app.run(debug=True)
