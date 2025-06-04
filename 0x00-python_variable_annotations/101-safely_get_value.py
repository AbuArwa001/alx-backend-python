#!/usr/bin/env python3
"""
This module provides a function
'safely_get_value' that attempts to retrieve a value
from a mapping using a specified key.
If the key is not found, it returns a default value.
"""

from typing import Any, Mapping, Sequence, TypeVar, Union

T = TypeVar('T')


def safely_get_value(
    dct: Mapping,
    key: Any,
    default: Union[T, None] = None
) -> Union[Any, T]:
    """
    Attempt to retrieve a value from a mapping using a key,
    or return a default value.

    Args:
        dct (Mapping[Any, T]): The mapping from which to retrieve the value.
        key (Any): The key to look up in the mapping.
        default (Union[T, None]): The default value
        to return if the key is not found.

    Returns:
        Union[T, None]: The value associated with
        the key, or the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
