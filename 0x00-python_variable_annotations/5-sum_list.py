#!/usr/bin/env python3
from typing import List

"""
Module to define a function that calculates the sum of
all elements in a list of floats.
"""


def sum_list(input_list: List[float]) -> float:
    """
    Calculate the sum of all elements in a list of floats.

    Args:
        input_list (List[float]): A list of floating point numbers.

    Returns:
        float: The sum of all elements in the list.
    """
    return sum(input_list)
