#!/usr/bin/env python3
"""
Database connection using context manager.
This script defines a context manager to handle database connections.
The context manager automatically connects to the database and closes the connection
when exiting the context.
Usage:
    with DatabaseConnection('users.db') as conn:
        # Perform database operations
        pass
"""
import sqlite3
from contextlib import contextmanager
from typing import Generator, Optional
import functools
import logging
import time
from datetime import datetime
from sqlite3 import Connection, Cursor
from sqlite3.dbapi2 import Error

class DatabaseConnection:
    """Context manager for database connection."""
    def __init__(self, db_file: str):
        self.db_file = db_file
        self.conn: Optional[Connection] = None

    def __enter__(self) -> Connection:
        self.conn = sqlite3.connect(self.db_file)
        return self.conn

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        if self.conn:
            self.conn.close()
            self.conn = None
        if exc_type is not None:
            # Handle exceptions if needed
            print(f"Exception occurred: {exc_value}")


with DatabaseConnection('users.db') as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    results = cursor.fetchall()
    print(results)
