from flask import Flask, render_template, request
from Server.Login_SignUp import handle_sign_up, handle_login
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
import os

secret_key = os.urandom(32)
app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = secret_key
jwt = JWTManager(app)
app.secret_key = "idan2001"


# Route for Home

@app.route("/index")
@app.route('/')
@jwt_required(optional=True)
def index():
    user_name = get_jwt_identity() or "Guest"
    # Render the index.html template
    return render_template('index.html', user_name=user_name)


# Route for login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        return handle_login()


# Route for sign up
@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'GET':
        return render_template('sign_up.html')
    elif request.method == 'POST':
        return handle_sign_up()


@app.route('/dashboard')
def dashboard():
    return 'Welcome to the Dashboard!'


# Route for catalog
@app.route('/catalog', methods=['GET'])
@jwt_required(optional=True)
def catalog():
    user_name = get_jwt_identity() or "Guest"
    return render_template('catalog.html', user_name=user_name)


@app.route('/contact', methods=['GET'])
@jwt_required(optional=True)
def contact():
    user_name = get_jwt_identity() or "Guest"
    return render_template('contact.html', user_name=user_name)


if __name__ == '__main__':
    app.run(debug=True)
