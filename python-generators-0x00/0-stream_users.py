#!/usr/bin/env python3
"""Stream rows from the user_data table using a generator"""

import mysql.connector

def stream_users():
    """Generator that yields one row at a time from user_data table"""
    connection = mysql.connector.connect(
        host="localhost",
        user="root",      
        password="Muthike#85", 
        database="ALX_prodev"
    )

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM user_data")

    while True:
        row = cursor.fetchone()
        if row is None:
            break
        yield row

    cursor.close()
    connection.close()
