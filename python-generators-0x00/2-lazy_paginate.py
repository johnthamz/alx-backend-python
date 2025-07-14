# 2-lazy_paginate.py

import mysql.connector
from seed import connect_to_prodev

def paginate_users(page_size, offset):
    """
    Helper function to fetch a page of users starting from a specific offset.
    """
    connection = connect_to_prodev()
    cursor = connection.cursor()
    query = "SELECT * FROM user_data LIMIT %s OFFSET %s"
    cursor.execute(query, (page_size, offset))
    rows = cursor.fetchall()
    cursor.close()
    connection.close()
    return rows

def lazy_paginate(page_size):
    """
    Generator that fetches one page at a time using the paginate_users function.
    """
    offset = 0
    while True:
        users = paginate_users(page_size, offset)
        if not users:
            break
        yield users
        offset += page_size
