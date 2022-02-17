import mysql.connector as mysql
from mysql.connector import Error

try:
    # Try to establish connection with database
    connection = mysql.connect(
    host="oege.ie.hva.nl",
    user="arslanm4",
    password="/5iy+CTv39kVZQ",
    database="zarslanm4",
    port=3306)

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
