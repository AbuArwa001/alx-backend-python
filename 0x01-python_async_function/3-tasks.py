#!/usr/bin/env python3
"""
This module contains a function for
creating an asyncio task that waits for a random delay.
"""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int):
    """
    Creates an asyncio task that waits for
    a random delay between 0 and max_delay (inclusive).

    Args:
        max_delay (int): The maximum delay in seconds.

    Returns:
        asyncio.Task: An asyncio task
        representing the asynchronous operation.
    """
    return asyncio.create_task(wait_random(max_delay))
