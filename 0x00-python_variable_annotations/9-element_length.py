#!/usr/bin/env python3
"""
This module provides a function 'element_length'
that takes a sequence of sequences
and returns a list of tuples, each
containing a sequence and its corresponding length.
"""
from typing import  Sequence, Tuple, List, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Return a list of tuples with each sequence and its length.

    Args:
        lst (Sequence[Sequence]): A sequence of sequences.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples,
        each containing a sequence and its length.
    """
    return [(i, len(i)) for i in lst]
