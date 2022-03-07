from db import connection
import streamlit as sl
import pandas as pd

if connection.is_connected():
    cursor = connection.cursor()
    cursor.execute("select database();")
    print("You're connected to database in main: ", cursor.fetchone())


header = sl.container()
dataset = sl.container()

with header:
    sl.title('Hallo Big Data')

with dataset:
    amsterdam_data = pd.read_csv('data/h-amsterdam.csv')

    sl.write(amsterdam_data.head(100))