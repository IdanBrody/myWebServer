from flask import Flask, render_template, request
from Server.Login_SignUp import handle_sign_up, handle_login


app = Flask(__name__)
app.secret_key = "idan2001"

# Route for Home
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


if __name__ == '__main__':
    app.run(debug=True)
