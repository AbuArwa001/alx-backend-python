#!/usr/bin/env python3
"""
This module provides a utility function 'to_kv' that takes a key (str)
and a value (int or float).
It returns a tuple with the key and the square of the value.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Return a tuple with the key and the square of the value.

    Args:
        k (str): The key to be included in the tuple.
        v (Union[int, float]): The value to be squared and
                               included in the tuple.

    Returns:
        Tuple[str, float]: A tuple containing the key
                           and the square of the value.
    """
    return (k, v**2)
