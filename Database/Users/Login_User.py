from Database.MySQL_Connection import connect_to_database
from passlib.hash import sha256_crypt


def login_user(username, password):
    # Get a connection to the database
    connection = connect_to_database()
    # Create a cursor object to execute SQL queries
    cursor = connection.cursor()
    # SQL query to check if the user exists
    query = "SELECT password FROM users WHERE username = '{}'".format(username)
    # Execute the query and fetch the result
    cursor.execute(query)
    result = cursor.fetchone()
    # Close the cursor and connection
    cursor.close()
    connection.close()

    # Check if the result is not None (user exists) and password is correct
    if result is not None and sha256_crypt.verify(password, result[0]):
        return True
    else:
        return False

