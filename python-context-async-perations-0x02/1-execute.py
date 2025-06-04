#!/usr/bin/env python3
"""
1-execute.py
Execute a SQL query using a database connection.
This script defines a function to execute a SQL query using a database connection.
The function can be used to execute any SQL query.
Usage:
    execute_query(conn, query)
"""

import sqlite3
from typing import Any, List, Optional, Tuple


class ExecuteQuery:
    """Context manager for executing parameterized SQL queries."""
    
    def __init__(self, db_path: str, query: str, params: Tuple[Any, ...] = ()):
        """
        Initialize the ExecuteQuery context manager.
        
        Args:
            db_path: Path to the SQLite database file
            query: SQL query string (can contain parameters)
            params: Tuple of parameters for the query
        """
        self.db_path = db_path
        self.query = query
        self.params = params
        self.conn: Optional[sqlite3.Connection] = None
        self.cursor: Optional[sqlite3.Cursor] = None
        self.results: Optional[List[Tuple]] = None
    
    def __enter__(self) -> List[Tuple]:
        """
        Establish database connection and execute query when entering context.
        
        Returns:
            List of tuples containing query results
        """
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()
        
        try:
            self.cursor.execute(self.query, self.params)
            self.results = self.cursor.fetchall()
            return self.results
        except sqlite3.Error as e:
            print(f"Error executing query: {e}")
            return []
    
    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        """
        Clean up database resources when exiting context.
        
        Args:
            exc_type: Exception type if any occurred
            exc_val: Exception value if any occurred
            exc_tb: Traceback if any occurred
        """
        if self.cursor:
            self.cursor.close()
        if self.conn:
            if exc_type is None:
                self.conn.commit()
            else:
                self.conn.rollback()
            self.conn.close()

# Example usage
if __name__ == "__main__":
    # Using the context manager with our specific query
    with ExecuteQuery(
        db_path="users.db",
        query="SELECT * FROM users WHERE age > ?",
        params=(25,)
    ) as results:
        print("Users over 25 years old:")
        for row in results:
            print(row)