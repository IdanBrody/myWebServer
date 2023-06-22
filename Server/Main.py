from flask import Flask, render_template, request

import Database.MySQL_Connection
from Server.Login_SignUp import handle_sign_up, handle_login



app = Flask(__name__)
app.secret_key = "idan2001"

# Route for Home
@app.route("/index")
@app.route('/')
def index():
    # Render the index.html template
    return render_template('index.html')


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
def catalog():
    connection = Database.MySQL_Connection.connect_to_database()
    cursor = connection.cursor()
    query = "SELECT product_link FROM products"
    cursor.execute(query)
    products = [{'image_link': row[0]} for row in cursor.fetchall()]
    return render_template('catalog.html', products=products)

@app.route('/contact', methods=['GET'])
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
