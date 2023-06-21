from Database.MySQL_Connection import connect_to_database


def login_user(username, password):
    # Get a connection to the database
    connection = connect_to_database()

    # Create a cursor object to execute SQL queries
    cursor = connection.cursor()

    # SQL query to check if the user exists
    query = "SELECT * FROM users WHERE username = %s AND password = %s"
    values = (username, password)

    # Execute the query and fetch the result
    cursor.execute(query, values)
    result = cursor.fetchone()

    # Close the cursor and connection
    cursor.close()
    connection.close()

    # Check if the result is not None (user exists)
    if result is not None:
        return True
    else:
        return False
