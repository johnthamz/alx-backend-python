#!/usr/bin/env python3
from datetime import datetime
import sqlite3
import functools

def log_queries(func):
    """Decorator to log SQL queries"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        query = args[0] if args else "NO QUERY PROVIDED"
        print(f"[{datetime.now()}] Executing SQL Query: {query}")
        return func(*args, **kwargs)
    return wrapper

@log_queries
def execute_query(query):
    conn = sqlite3.connect("test.db")
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    execute_query("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT);")
