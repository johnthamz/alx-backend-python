#!/usr/bin/env python3
import sqlite3
import functools
import time
import random  # For simulating transient failures

def retry_on_failure(retries=3, delay=2):
    """Decorator that retries a function if it fails due to an exception."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempt = 0
            while attempt < retries:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Attempt {attempt + 1} failed: {e}")
                    attempt += 1
                    if attempt < retries:
                        print(f"Retrying in {delay} seconds...")
                        time.sleep(delay)
                    else:
                        print("All attempts failed.")
                        raise e
        return wrapper
    return decorator

# Example usage
@retry_on_failure(retries=3, delay=2)
def unstable_operation():
    """This function randomly fails to simulate transient DB error"""
    if random.choice([True, False]):
        raise sqlite3.OperationalError("Simulated DB connection error.")
    print("Query succeeded!")

if __name__ == "__main__":
    unstable_operation()
