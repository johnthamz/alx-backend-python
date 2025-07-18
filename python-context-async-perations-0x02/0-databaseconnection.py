#!/usr/bin/env python3
import sqlite3

class DatabaseConnection:
    """Custom context manager to handle DB connection"""

    def __init__(self, db_name="example.db"):
        self.db_name = db_name
        self.conn = None

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_name)
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.conn:
            self.conn.close()

# Usage of the context manager
if __name__ == "__main__":
    with DatabaseConnection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users;")
        results = cursor.fetchall()
        print("Results from DB:")
        for row in results:
            print(row)
