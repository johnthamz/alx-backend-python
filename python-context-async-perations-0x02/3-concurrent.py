#!/usr/bin/env python3
import asyncio
import aiosqlite

DB_NAME = "example.db"

# Fetch all users
async def async_fetch_users():
    async with aiosqlite.connect(DB_NAME) as db:
        async with db.execute("SELECT * FROM users") as cursor:
            users = await cursor.fetchall()
            print("All users:")
            for row in users:
                print(row)

# Fetch users older than 40
async def async_fetch_older_users():
    async with aiosqlite.connect(DB_NAME) as db:
        async with db.execute("SELECT * FROM users WHERE age > 40") as cursor:
            users = await cursor.fetchall()
            print("Users older than 40:")
            for row in users:
                print(row)

# Run both concurrently
async def fetch_concurrently():
    await asyncio.gather(
        async_fetch_users(),
        async_fetch_older_users()
    )

# Start the event loop
if __name__ == "__main__":
    asyncio.run(fetch_concurrently())
