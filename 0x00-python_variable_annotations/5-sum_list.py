#!/usr/bin/env python3
from typing import List
"""
Module to Define a function that
Calculate the sum of all elements
"""


def sum_list(input_list: List[float]) -> float:
    """
    Calculate the sum of all elements
    """
    total: float = 0
    for i in input_list:
        total += i
    return total
