#!/usr/bin/env python3
"""
This module contains an asynchronous comprehension
function that generates a list of values from an async generator.
"""
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Generates a list of values using an asynchronous comprehension.

    Returns:
        List[float]: List of random values between 0 and 10.
    """
    return [generator async for generator in async_generator()]
