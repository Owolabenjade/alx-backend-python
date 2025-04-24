#!/usr/bin/env python3
"""Module for creating a tuple from a string and number."""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple with the string k and the square of v.

    Args:
        k: A string to be used as the first element of the tuple
        v: An int or float to be squared and used as the second element

    Returns:
        A tuple where the first element is the string k and the second
        element is the square of v as a float
    """
    return (k, float(v ** 2))