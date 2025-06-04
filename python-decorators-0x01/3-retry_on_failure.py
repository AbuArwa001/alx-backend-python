#!/usr/bin/env python3
"""
3-retry_on_failure.py
Retry a function on failure.
This script defines a decorator to retry a function on failure.
The decorator can be applied to any function that may fail.
"""
import functools
import sqlite3
import time

#### paste your with_db_decorator here
with_db_connection = __import__('1-with_db_connection').with_db_connection

def retry_on_failure(retries=3, delay=1):
    """Decorator to retry a function on failure."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Attempt {attempt + 1} failed: {e}")
                    time.sleep(delay)
            raise Exception("All attempts failed.")
        return wrapper
    return decorator

@with_db_connection
@retry_on_failure(retries=3, delay=1)
def fetch_users_with_retry(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()

#### attempt to fetch users with automatic retry on failure

users = fetch_users_with_retry()
print(users)
