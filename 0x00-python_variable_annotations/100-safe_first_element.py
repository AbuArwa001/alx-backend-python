#!/usr/bin/env python3
"""
This module provides a utility function
    'safe_first_element' that safely retrieves
the first element of a sequence without
    raising an error if the sequence is empty.
"""

from typing import Union, Sequence, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Safely return the first element of a
        sequence or None if it's empty.
    Args:
        lst (Sequence[Any]): A sequence
              from which the first element is to be retrieved.

    Returns:
        Union[Any, None]: The first element of
            the sequence, or None if the sequence is empty.
    """
    if lst:
        return lst[0]
    else:
        return None
