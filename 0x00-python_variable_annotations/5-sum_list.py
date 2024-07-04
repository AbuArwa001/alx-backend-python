#!/usr/bin/env python3
"""
Module to Define values
"""


def sum_list(input_list: list[float]) -> float:
    total : float = 0
    for i in input_list:
        total += i
    return total