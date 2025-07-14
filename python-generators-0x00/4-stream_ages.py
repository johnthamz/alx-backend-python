# seed.py
import mysql.connector

def connect_to_prodev():
    return mysql.connector.connect(
        host="localhost",
        user="root",         # Replace with your actual MySQL user
        pas@Muthike#85sword="",         # Replace with your actual password
        database="ALX_prodev
# 4-stream_ages.py

from seed import connect_to_prodev

def stream_user_ages():
    """Generator that yields user ages one by one from user_data."""
    connection = connect_to_prodev()
    cursor = connection.cursor()
    cursor.execute("SELECT age FROM user_data")

    for (age,) in cursor:
        yield age

    cursor.close()
    conn

def compute_average_age():
    total = 0
    count = 0

    for age in stream_user_ages():
        total += age
        count += 1

    if count == 0:
        print("No users found.")
    else:
        average = total / count
        print(f"Average age of users: {average:.2f}")
ection.close()
"
    )
