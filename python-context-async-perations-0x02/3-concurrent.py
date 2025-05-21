#!/usr/bin/env python3
"""
3-concurrent.py
"""
import aiosqlite
import asyncio
import functools
from typing import List, Dict, Any

async def async_fetch_users():
    """Asynchronous function to fetch users from the database."""
    async with aiosqlite.connect('users.db') as conn:
        cursor = await conn.execute("SELECT * FROM users")
        rows = await cursor.fetchall()
        return rows
async def async_fetch_older_users():
    """Asynchronous function to fetch users older than 25."""
    async with aiosqlite.connect('users.db') as conn:
        cursor = await conn.execute("SELECT * FROM users WHERE age > 40")
        rows = await cursor.fetchall()
        return rows
async def fetch_concurrently():
    data = await asyncio.gather(
        async_fetch_users(),
        async_fetch_older_users()
    )
    print(data)

asyncio.run(fetch_concurrently())
