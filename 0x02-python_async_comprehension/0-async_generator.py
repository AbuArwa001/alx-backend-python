#!/usr/bin/env python3
"""
This module contains an asynchronous generator function
that yields random values between 0 and 10.
"""
import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronous generator that yields random values between 0 and 10.

    Yields:
        float: Random value between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
