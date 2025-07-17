#!/usr/bin/env python3
import sqlite3
import functools

def with_db_connection(func):
    """Opens and closes DB connection, passes cursor"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect("example.db")
        cursor = conn.cursor()
        try:
            result = func(cursor, conn, *args, **kwargs)
            return result
        finally:
            conn.close()
    return wrapper

def transactional(func):
    """Decorator to manage DB transactions: commit or rollback"""
    @functools.wraps(func)
    def wrapper(cursor, conn, *args, **kwargs):
        try:
            result = func(cursor, conn, *args, **kwargs)
            conn.commit()
            return result
        except Exception as e:
            conn.rollback()
            print("Transaction failed! Rolled back.")
            print("Error:", e)
            return None
    return wrapper

# Example usage:
@with_db_connection
@transactional
def insert_user(cursor, conn, name):
    cursor.execute("INSERT INTO users (name) VALUES (?);", (name,))
    # Simulate error to test rollback:
    # raise Exception("Fail!")

if __name__ == "__main__":
    insert_user("Alice")
    print("Done.")
