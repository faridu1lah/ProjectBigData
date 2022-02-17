import pandas as pd
import mysql.connector

mydb = mysql.connector.connect(
    host="oege.ie.hva.nl",
    user="fariduf",
    password="I.RdiJt.qS.otf",
    database="zfariduf",
    port=3306,
)

mycursor = mydb.cursor()

mycursor.execute(
    "CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))"
)

print(mydb)
