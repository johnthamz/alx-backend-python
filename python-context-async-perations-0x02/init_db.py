import sqlite3

conn = sqlite3.connect("example.db")
cursor = conn.cursor()

# Drop the table to reset
cursor.execute("DROP TABLE IF EXISTS users")

# Create the users table with name and age
cursor.execute("""
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL
)
""")

# Insert users with both name and age
cursor.execute("INSERT INTO users (name, age) VALUES ('Jane Doe', 32)")
cursor.execute("INSERT INTO users (name, age) VALUES ('Alice', 45)")
cursor.execute("INSERT INTO users (name, age) VALUES ('Bob', 22)")

conn.commit()
conn.close()

print("users table created with age column and data inserted.")

