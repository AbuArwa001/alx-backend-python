#!/usr/bin/env python3
"""
Module to implement callables
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create a closure that multiplies a given number by a predefined multiplier.

    Args:
        multiplier (float): The multiplier value.

    Returns:
        Callable[[float], float]:
                    A function that multiplies its input by the multiplier.
    """
    def multiplier_function(value: float) -> float:
        """
        Multiply the given value by the multiplier.

        Args:
            value (float): The value to be multiplied.

        Returns:
            float: The result of the multiplication.
        """
        return value * multiplier
    return multiplier_function
