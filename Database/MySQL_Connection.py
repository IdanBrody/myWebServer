import os

import mysql.connector


def connect_to_database():
    # MySQL server connection details
    host = os.environ.get('MYSQL_HOST')
    port = 3306
    username = os.environ.get('MYSQL_USER')
    password = os.environ.get('MYSQL_PASSWORD')
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

