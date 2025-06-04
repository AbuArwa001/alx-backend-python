#!/usr/bin/env python3
import os
from typing import Any, Dict, Generator, List

import mysql.connector

seed = __import__('seed')
stream_user_ages = __import__('4-stream_ages').stream_user_ages

"""
Module to stream user data from a CSV file.
This module contains a generator function that reads user data from a CSV file
and yields each row as a dictionary.
"""
@stream_user_ages
def stream_users()-> Generator[Any, None, None]:
    """Generator function to stream user data from a user_data table file."""

    # connect to the MySQL database
    connection = seed.connect_to_prodev()
    if connection:
        # create a cursor object
        cursor = connection.cursor()

        # execute a query to select all rows from the user_data table
        cursor.execute("SELECT * FROM user_data")

        # fetch all rows from the result set
        rows = cursor.fetchall()

        # get the column names from the cursor description
        column_names = [i[0] for i in cursor.description]

        # iterate over the rows and yield each row as a dictionary
        for row in rows:
            yield {
                'user_id': row[0],
                'name': row[1],
                'email': row[2],
                'age': int(row[3]),
            }

        # close the cursor and connection
        cursor.close()
        connection.close()
    else:
        print("Failed to connect to the database.")
        return None
    # if the connection fails, return an empty generator
    return iter([])
    
