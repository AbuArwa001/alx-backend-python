#!/usr/bin/env python3

"""
This module contains an asynchronous coroutine
for demonstrating async and await syntax in Python.

The module provides the following function:
- wait_random: An asynchronous coroutine
that waits for a random delay and returns the delay.

Functions:
    wait_random(max_delay: int = 10) -> float
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Waits for a random delay between
    1 and max_delay seconds (inclusive) and returns the actual delay.

    Args:
        max_delay (int): The maximum delay in seconds. Default is 10.

    Returns:
        float: The actual delay in seconds.
    """
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
