from mysql.connector import Error
from config.config import mysql
from sqlalchemy import create_engine

try:
    # Try to establish connection with database
    connection = create_engine(f"mysql+mysqlconnector://{mysql['user']}:{mysql['password']}@{mysql['host']}/{mysql['database']}")
    data = connection.execute("select database();")
    print(f"Connected to database: {data.fetchone()[0]}")
# Catch any errors thrown and print it
except Error as e:
    print("Error while connecting to MySQL database: ", e)
