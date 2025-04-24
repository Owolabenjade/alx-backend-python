#!/usr/bin/env python3
"""Module for safely getting a value from a dictionary."""

from typing import Mapping, Any, TypeVar, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    """Return a value from a dict safely.

    Args:
        dct: A dictionary-like object
        key: A key to look up in the dictionary
        default: A default value to return if the key is not found

    Returns:
        The value associated with the key if found, otherwise the default value
    """
    if key in dct:
        return dct[key]
    else:
        return default