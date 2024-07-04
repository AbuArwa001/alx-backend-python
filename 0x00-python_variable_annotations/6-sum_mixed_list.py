#!/usr/bin/env python3
"""
Module to define a function that calculates the sum of
all elements in a list of floats.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculate the sum of all elements in a list of floats.

    Args:
        input_list (List[float]): A list of floating point numbers.

    Returns:
        float: The sum of all elements in the list.
    """
    return sum(mxd_lst)
