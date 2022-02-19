from db import connection

if connection.is_connected():
    cursor = connection.cursor()
    cursor.execute("select database();")
    print("You're connected to database in main: ", cursor.fetchone())
