import mysql.connector


def connect_to_database():
    # MySQL server connection details
    host = 'localhost'
    port = 3306
    username = 'root'
    password = 'Idan2001!'
    database = 'shoe_store'

    # Establish connection to MySQL server
    connection = mysql.connector.connect(
        host=host,
        port=port,
        user=username,
        password=password,
        database=database
    )

    return connection

