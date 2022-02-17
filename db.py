import pandas as pd
import mysql.connector as mysql

mydb = mysql.connect(
    host="oege.ie.hva.nl",
    user="fariduf",
    password="I.RdiJt.qS.otf",
    database="zfariduf",
    port=3306,
)

mycursor = mydb.cursor()

#  als je dit aan zit wordt een table toegevoegd
# mycursor.execute(
#     "CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))"
# )

print(mydb)
