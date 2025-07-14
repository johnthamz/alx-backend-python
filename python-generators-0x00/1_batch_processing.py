import mysql.connector

def connect_to_prodev():
    return mysql.connector.connect(
        host="localhost",
        user="your_mysql_username",       # Replace with your username
        password="your_mysql_password",   # Replace with your password
        database="ALX_prodev"
    )

def stream_users_in_batches(batch_size):
    connection = connect_to_prodev()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM user_data;")
    
    while True:
        batch = cursor.fetchmany(size=batch_size)
        if not batch:
            break
        yield batch

    cursor.close()
    connection.close()

def batch_processing(batch_size):
    for batch in stream_users_in_batches(batch_size):
        filtered = [user for user in batch if user[3] > 25]  # index 3 = age
        yield filtered
