import functools

def log_queries():
    """Decorator that logs the SQL query used inside a function"""

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Assume the SQL is the first argument
            sql_query = args[0] if args else "NO QUERY PROVIDED"   

            print(f"Executing SQL query: {sql_query}")
            return func (*args, **kwargs)

        return wrapper
    
    return decorator

   
   #  EXAMPLE FUNCTION FOR TESTING
@log_queries()
def execute_query(query):
    # Simulate running the query (we're not using a real DB yet)
    print("Running query on the database...")

#  RUN TEST
if __name__ == "__main__":
    execute_query("SELECT * FROM users;")