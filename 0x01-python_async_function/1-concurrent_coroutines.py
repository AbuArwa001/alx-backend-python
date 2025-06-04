#!/usr/bin/env python3
"""
This module contains an asynchronous function for waiting random durations.
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns `n` tasks of `wait_random` with the specified `max_delay`.
    Returns a list of delays (float values) in ascending order.
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delays = [await task for task in tasks]
    return sorted(delays)
