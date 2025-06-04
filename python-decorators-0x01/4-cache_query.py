#!/usr/bin/env python3
"""
4-cache_query.py
Cache SQL query results using a decorator.
This script defines a decorator to cache SQL query results.
The decorator can be applied to any function that executes SQL queries.
The decorator caches the results of the SQL query in a dictionary.
Usage:
    @cache_query
    def fetch_users_with_cache(conn, query):
        # Function to fetch users from the database
        pass

    if __name__ == "__main__":
        # Example usage
        users = fetch_users_with_cache(query="SELECT * FROM users")
        print(users)
"""
import functools
from datetime import datetime

with_db_connection = __import__('1-with_db_connection').with_db_connection

query_cache = {}

def cache_query(func):
    """Decorator to cache query results with expiration."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Extract query from either args or kwargs
        query = kwargs.get('query')
        if query is None and len(args) > 1:
            query = args[1]  # For conn, query signature
        
        if not query:
            raise ValueError("Query parameter not found")
        
        # Check cache
        cache_entry = query_cache.get(query)
        if cache_entry:
            cached_time, result = cache_entry
            # if datetime.now() - cached_time <  300:  # Cache expiration time (5 minutes)
            print("Using cached result")
            return result
            # del query_cache[query]  # Remove expired cache
        
        # Execute and cache
        print("Executing and caching query")
        result = func(*args, **kwargs)
        query_cache[query] = (datetime.now(), result)
        return result
    return wrapper

@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

#### First call will cache the result
users = fetch_users_with_cache(query="SELECT * FROM users")

#### Second call will use the cached result
users_again = fetch_users_with_cache(query="SELECT * FROM users")
