#!/usr/bin/env python3
"""
2-transactional.py
Transactional decorator for database operations.
This script defines a decorator to handle transactions automatically.
The decorator can be applied to any function that performs database operations.
Usage:
    @with_db_connection
    @transactional
    def update_user_email(conn, user_id, new_email):
        # Function to update a user's email in the database
        pass

    if __name__ == "__main__":
        # Example usage
        update_user_email(user_id=1,

"""
import sqlite3 
import functools

with_db_connection = __import__('1-with_db_connection').with_db_connection

def transactional(func):
    """Decorator to handle transactions automatically."""
    @functools.wraps(func)
    def wrapper(conn, *args, **kwargs):
        try:
            # Start a transaction
            conn.execute("BEGIN")
            # Call the original function
            result = func(conn, *args, **kwargs)
            # Commit the transaction
            conn.commit()
            return result
        except Exception as e:
            # Rollback the transaction in case of an error
            conn.rollback()
            print(f"Transaction failed: {e}")
    return wrapper


@with_db_connection 
@transactional
def update_user_email(conn, user_id, new_email): 
    cursor = conn.cursor() 
    cursor.execute("UPDATE users SET email = ? WHERE id = ?", (new_email, user_id)) 
    #### Update user's email with automatic transaction handling 

update_user_email(user_id=1, new_email='Crawford_Cartwright@hotmail.com')