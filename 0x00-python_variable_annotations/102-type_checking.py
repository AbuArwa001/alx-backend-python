#!/usr/bin/env python3
"""
A module for zooming in on arrays.

This module provides a function that duplicates elements in a tuple
based on a specified factor, effectively 'zooming in' on the array.
"""

from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Duplicate each element in a tuple by a specified factor.
    Args:
        lst (Tuple): The original tuple of elements to be duplicated.
        factor (int, optional): The number of times each element
        is to be duplicated. Defaults to 2.
    Returns:
        List: A list with elements from the
        original tuple duplicated by the specified factor.
    """
    zoomed_in: List = [
        item for item in lst
        for _ in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(tuple(array))

zoom_3x = zoom_array(tuple(array), 3)
