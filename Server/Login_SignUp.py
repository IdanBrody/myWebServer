from flask import render_template, flash, redirect, request, url_for, session
from Database.Users.Creating_User import create_user, check_user_exists, check_email_exists
from Database.Users.Login_User import login_user
from passlib.hash import sha256_crypt
from flask_jwt_extended import create_access_token


def handle_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Check the credentials using login_user function
        if login_user(username, password):
            # Authentication successful
            access_token = create_access_token(identity=username)
            session['user_name'] = username
            session['logged_in'] = True
            session['Shopping_Cart'] = []
            flash('Login successful!', 'success')
            return redirect(url_for('index'))
        else:
            # Authentication failed
            flash('Invalid username or password. Please try again.', 'error')
            return redirect(url_for('login'))

        # For GET requests, render the login page
    return render_template('login.html')


def handle_sign_up():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        # Check if username already exists in the database
        if check_user_exists(username):
            flash('Username already exists. Please choose a different username.', 'error')
            return redirect('/sign_up')  # Replace '/sign_up' with your desired sign-up page URL

        # Check if email already exists in the database
        if check_email_exists(email):
            flash('Email already exists. Please use a different email.', 'error')
            return redirect(url_for('sign_up'))

        # encrypt the password
        password = sha256_crypt.encrypt(password)

        # Create the user in the database
        create_user(username, password, email)

        flash('Account created successfully. You can now login.', 'success')
        return redirect('/login')  # Replace '/login' with your login page URL

    return redirect('/sign_up')  # Replace '/sign_up' with your desired sign-up page URL
