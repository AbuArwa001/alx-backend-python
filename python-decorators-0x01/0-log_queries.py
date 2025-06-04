#!/usr/bin/env python3
"""
0-log_queries.py
Log SQL queries using a decorator.
This script defines a decorator to log SQL queries executed in a function.
It uses the logging module to log the queries with a timestamp.
The decorator can be applied to any function that executes SQL queries.
The decorator logs the SQL query before executing it.
Usage:
    @log_queries
    def fetch_all_users(query):
        # Function to fetch all users from the database
        pass

    if __name__ == "__main__":
        # Example usage
        query = "SELECT * FROM users"
        users = fetch_all_users(query)
    # print(users)
    # Example usage
    query = "SELECT * FROM users"
    users = fetch_all_users(query)
    # print(users)
"""
import functools
import sqlite3
from datetime import datetime
from logging import Formatter, StreamHandler, getLogger

# Set up logging
#### decorator to lof SQL queries

def log_queries(func) -> None:
    """Decorator to log SQL queries."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> None:
         """Wrapper function to log SQL queries."""
         # Log the SQL query
         logger = getLogger(__name__)
         handler = StreamHandler()
         datetime_format = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
         formatter = Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt=datetime_format)
        #  handler.setFormatter()
         handler.setFormatter(formatter)
         logger.addHandler(handler)
         logger.setLevel('INFO')
         
         query = args[0]
         logger.info(f"Executing query: {query}")
         
         # Call the original function
         return func(*args, **kwargs)
    return wrapper

@log_queries
def fetch_all_users(query)-> None:
    """Fetch all users from the database."""
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

# if __name__ == "__main__":
#     # Example usage
#     query = "SELECT * FROM users"
#     users = fetch_all_users(query)
#     # print(users)
# #### fetch users while logging the query
users = fetch_all_users(query="SELECT * FROM users")
