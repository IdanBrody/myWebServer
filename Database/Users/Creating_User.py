from Database.MySQL_Connection import connect_to_database
import mysql.connector


def check_user_exists(username):
    # Get a connection to the database
    connection = connect_to_database()

    # Create a cursor object to execute SQL queries
    cursor = connection.cursor()

    try:
        # Check if the username already exists
        query = "SELECT * FROM users WHERE username = %s"
        value = (username,)
        cursor.execute(query, value)
        result = cursor.fetchone()

        # If the result is not None, the username already exists
        if result is not None:
            return True
        else:
            return False
    except mysql.connector.Error as error:
        print("Error checking if user exists:", error)
        return False
    finally:
        # Close the cursor and connection
        cursor.close()
        connection.close()


def check_email_exists(email):
    # Get a connection to the database
    connection = connect_to_database()

    # Create a cursor object to execute SQL queries
    cursor = connection.cursor()

    # SQL query to check if the email exists
    query = "SELECT * FROM users WHERE email = %s"
    value = (email,)

    # Execute the query and fetch the result
    cursor.execute(query, value)
    result = cursor.fetchone()

    # Close the cursor and connection
    cursor.close()
    connection.close()

    # Check if the result is not None (email exists)
    if result is not None:
        return True
    else:
        return False


def create_user(username, password, email):
    # Get a connection to the database
    connection = connect_to_database()

    # Create a cursor object to execute SQL queries
    cursor = connection.cursor()

    try:
        # Check if the user already exists
        if check_user_exists(username):
            print("Username already exists!")
            return False

        # Username does not exist, proceed with creating the user
        # SQL query to insert a new user into the "users" table
        query = "INSERT INTO users (username, password, email) VALUES (%s, %s, %s)"
        values = (username, password, email)

        # Execute the SQL query
        cursor.execute(query, values)

        # Commit the transaction to save the changes
        connection.commit()

        print("User created successfully!")
        return True
    except mysql.connector.Error as error:
        print("Error creating user:", error)
        connection.rollback()
        return False
    finally:
        # Close the cursor and connection
        cursor.close()
        connection.close()
