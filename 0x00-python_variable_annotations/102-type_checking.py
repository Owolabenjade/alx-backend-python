#!/usr/bin/env python3
"""Module for demonstrating type checking with mypy."""

from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Return a zoomed-in version of a tuple.

    Args:
        lst: A tuple of elements to be duplicated
        factor: The number of times to duplicate each element

    Returns:
        A list with each element of the input tuple repeated 'factor' times
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, int(3.0))