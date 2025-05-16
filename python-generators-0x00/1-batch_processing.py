#!/usr/bin/env python3
from typing import Any, Dict

seed = __import__('seed')

def stream_users_in_batches(batch_size):
    """Generator function to stream user data from a user_data table file in batches."""
    # connect to the MySQL database
    connection = seed.connect_db()
    
    # check if the connection was successful
    if connection:
        connection = seed.connect_to_prodev()
        # create a cursor object
        cursor = connection.cursor()

        # execute a query to select all rows from the user_data table
        cursor.execute("SELECT * FROM user_data")

        while True:
            # fetch a batch of rows from the result set
            rows = cursor.fetchmany(batch_size)
            if not rows:
                break

            # get the column names from the cursor description
            column_names = [i[0] for i in cursor.description]

            # iterate over the rows and yield each row as a dictionary
            for row in rows:
                yield {
                    'user_id': row[0],
                    'name': row[1],
                    'email': row[2],
                    'age': row[3],
                }

        # close the cursor and connection
        cursor.close()
        connection.close()
    else:
        print("Failed to connect to the database.")
        return None
def batch_processing(batch_size) -> None:
    """Function to process user data in batches."""
    for batch in stream_users_in_batches(batch_size):
        # Process each batch of user data
        # print(batch)
        if batch.get('age') > 25:
            print(batch)
            # print(f"User {batch['name']} is older than 25.")
        # For example, you can save the batch to a file or perform some calculations
