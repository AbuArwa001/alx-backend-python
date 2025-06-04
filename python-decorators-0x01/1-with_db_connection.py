#!/usr/bin/env python3
"""
1-with_db_connection.py
Connect to a database and pass the connection to a function.
This script defines a decorator to connect to a database and pass the connection
to a function. The decorator handles the connection and disconnection automatically.
The decorator can be applied to any function that requires a database connection.
Usage:
    @with_db_connection
    def get_user_by_id(conn, user_id):
        # Function to fetch a user by ID from the database
        pass

    if __name__ == "__main__":
        # Example usage
        user = get_user_by_id(user_id=1)
        print(user)
"""
import functools
import sqlite3


def with_db_connection(func):
    """ Connect to the database and pass the connection to the function. """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Connect to the database
        conn = sqlite3.connect('users.db')
        try:
            # Call the original function with the connection
            return func(conn, *args, **kwargs)
        finally:
            # Close the connection
            conn.close()
    return wrapper 

@with_db_connection 
def get_user_by_id(conn, user_id): 
    cursor = conn.cursor() 
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,)) 
    return cursor.fetchone() 
    #### Fetch user by ID with automatic connection handling 

user = get_user_by_id(user_id=1)
print(user)