#!/usr/bin/env python3
"""
0-log_queries.py
YOUR CODE GOES HERE
"""
import sqlite3
import functools

#### decorator to lof SQL queries

def log_queries(func):
   def wrapper(*args, **kwargs):
         query = args[0]
         print(f"Executing query: {query}")
         result = func(*args, **kwargs)
         return result
   return wrapper

@log_queries
def fetch_all_users(query):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

if __name__ == "__main__":
    # Example usage
    query = "SELECT * FROM users"
    users = fetch_all_users(query)
    print(users)
# #### fetch users while logging the query
# users = fetch_all_users(query="SELECT * FROM users")
