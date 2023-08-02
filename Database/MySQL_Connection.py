import os

import mysql.connector


def connect_to_database():
    # MySQL server connection details
    host = os.environ.get('MYSQL_HOST', 'localhost')
    port = 3306
    username = os.environ.get('MYSQL_USER', 'root')
    password = os.environ.get('MYSQL_PASSWORD', 'Kuku1234!')
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

