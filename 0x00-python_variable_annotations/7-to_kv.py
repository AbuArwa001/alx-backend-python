#!/usr/bin/env python3
"""
This module provides a utility function to_kv that takes a key and a value.
The function returns a tuple with the key and the square of the value.
"""

from typing import Union


def to_kv(k: str, v: Union[int, float]) -> tuple:
    """
    Return a tuple with the key and the square of the value.

    Args:
        k (str): The key to be included in the tuple.
        v (Union[int, float]): The value to be squared and
                               included in the tuple.

    Returns:
        tuple: A tuple containing the key and the square of the value.
    """
    return (k, v**2)
