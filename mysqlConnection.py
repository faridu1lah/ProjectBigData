import mysql.connector as mysql
from mysql.connector import Error
import config


try:
    # Try to establish connection with database
    connection = mysql.connect(
        host=config.mysql["host"],
        user=config.mysql["user"],
        password=config.mysql["password"],
        database=config.mysql["database"],
        port=config.mysql["port"],
    )

    # If the connection is established print some data about the connection
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

# Catch any errors thrown and print it
except Error as e:
    print("Error while connecting to MySQL database: ", e)
