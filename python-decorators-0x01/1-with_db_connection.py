#!/usr/bin/env python3
import sqlite3
import functools

def with_db_connection(func):
    """Decorator that opens and closes a database connection."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Step 1: Connect to the database
        conn = sqlite3.connect("example.db")
        cursor = conn.cursor()

        try:
            # Step 2: Pass connection to the function
            result = func(cursor, *args, **kwargs)
            conn.commit()
        except Exception as e:
            print("Error:", e)
            conn.rollback()
            result = None
        finally:
            # Step 3: Close the connection
            conn.close()

        return result

    return wrapper


#  Example usage:
@with_db_connection
def create_table(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        );
    """)

@with_db_connection
def insert_user(cursor, name):
    cursor.execute("INSERT INTO users (name) VALUES (?);", (name,))


if __name__ == "__main__":
    create_table()
    insert_user("Jane Doe")
    print("User inserted.")
