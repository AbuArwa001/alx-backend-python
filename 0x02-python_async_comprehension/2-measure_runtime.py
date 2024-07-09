#!/usr/bin/env python3
"""
This module contains a function for measuring
the average execution time of concurrent coroutines.
"""

import asyncio
import time

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """
    Measures the total execution time for running multiple
    instances of async_comprehension concurrently.

    Returns:
        float: Average execution time per task.
    """
    start_time: float = time.perf_counter()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
    )
    end_time: float = time.perf_counter()
    return end_time - start_time
