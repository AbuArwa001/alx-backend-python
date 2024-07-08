#!/usr/bin/env python3
"""
This module contains a function for
measuring the average execution time of concurrent coroutines.
"""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for
    wait_n(n, max_delay) and returns the average time per task.

    Args:
        n (int): Number of tasks to spawn.
        max_delay (int): Maximum delay for each task.

    Returns:
        float: Average execution time per task.
    """
    start_time: float = time.time()
    asyncio.run(wait_n(n, max_delay))
    endtime: float = time.time()
    total_time = endtime - start_time
    return total_time / n
