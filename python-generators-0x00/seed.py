#!/usr/bin/python3
import mysql.connector
from decimal import Decimal
import csv

"""
This module contains functions to connect to a MySQL database,
create a database, create a table, and insert data into the table.
It uses the mysql-connector-python package to interact with the MySQL server.
The module provides the following functions:
- connect_db: Connect to the MySQL server.
- create_database: Create a new database if it doesn't exist.
- connect_to_prodev: Connect to the ALX_prodev database.
- create_table: Create a new table in the ALX_prodev database.
- insert_data: Insert data into the user_data table.
"""


def connect_db():
    """ Connect to the MySQL database """
    try:
        connection = mysql.connector.connect(
            user ='root',
            host='localhost',
            password='Khalif01#2023')
        if connection.is_connected():
            print("Connected to MySQL Server")
            return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def create_database(connection):
    """ Create a new database """
    try:
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
        # print("Database ALX_prodev created successfully")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
    
def connect_to_prodev():
    """ Connect to the ALX_prodev database """
    try:
        connection = connect_db()
        if connection:
            connection.database = 'ALX_prodev'
            print("Connected to ALX_prodev database")
            return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
    

def create_table(connection):
    """ Create a new table in the ALX_prodev database """
    try:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS user_data (
                user_id CHAR(36) PRIMARY KEY DEFAULT (UUID()),
                name VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL,
                age DECIMAL NOT NULL
            )
        """)
        # print("Table user_data created successfully")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()


def insert_data(connection, data):
    """ Insert data into the user_data table """
    try:
        cursor = connection.cursor()
        def insert(data):
            with open(data, 'r') as file:
                read_csv = csv.DictReader(file)
                next(read_csv,None)  # Skip the header line
                for line in read_csv:
                    yield line
                    # Assuming the CSV file has headers: name,email,age
                    # and the data is in the format: name,email,age
                    # Split the line by comma and unpack the values
                    # name, email ,age = line.strip().split(',')
        for line in insert(data):
            print(line)
            name, email ,age = line.get('name', None), line['email'], line['age']
            age = Decimal(age)
            cursor.execute("""
                INSERT INTO user_data (user_id, name, age, email)
                VALUES (UUID(), %s, %s, %s)
            """, (name, age, email))
        connection.commit()
        print("Data inserted successfully")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()