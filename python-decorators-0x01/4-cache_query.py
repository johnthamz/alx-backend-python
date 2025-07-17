#!/usr/bin/env python3
import sqlite3
import functools

# ✅ In-memory cache dictionary
query_cache = {}

def cache_query(func):
    """Decorator to cache SQL query results"""
    @functools.wraps(func)
    def wrapper(query):
        if query in query_cache:
            print(f"[CACHE HIT] Returning cached result for: {query}")
            return query_cache[query]

        print(f"[CACHE MISS] Executing and caching query: {query}")
        result = func(query)
        query_cache[query] = result
        return result
    return wrapper

@cache_query
def run_query(query):
    """Function to execute SQL query and return results"""
    conn = sqlite3.connect("example.db")
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    return result

if __name__ == "__main__":
    # Run twice to show cache in action
    print(run_query("SELECT * FROM users;"))
    print(run_query("SELECT * FROM users;"))  # Should hit cache


