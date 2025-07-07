# seed.py
import mysql.connector
import csv
import uuid

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="your_username",     # Replace with your MySQL username
        password="your_password"  # Replace with your MySQL password
    )

def create_database(connection):
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
    connection.commit()
    cursor.close()

def connect_to_prodev():
    return mysql.connector.connect(
        host="localhost",
        user="your_username",     # 🔁 Replace with your MySQL username
        password="your_password", # 🔁 Replace with your MySQL password
        database="ALX_prodev"
    )

def create_table(connection):
    cursor = connection.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS user_data (
        user_id VARCHAR(36) PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        age DECIMAL NOT NULL
    )
    """)
    connection.commit()
    cursor.close()
    print("Table user_data created successfully")

def insert_data(connection, csv_path):
    cursor = connection.cursor()
    with open(csv_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # skip header
        for row in reader:
            user_id = str(uuid.uuid4())
            name, email, age = row
            cursor.execute("""
            INSERT INTO user_data (user_id, name, email, age)
            VALUES (%s, %s, %s, %s)
            """, (user_id, name, email, age))
    connection.commit()
    cursor.close()

def stream_users(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM user_data")
    while True:
        row = cursor.fetchone()
        if row is None:
            break
        yield row
