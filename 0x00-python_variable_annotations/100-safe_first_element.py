#!/usr/bin/env python3
"""Module for safely getting the first element of a sequence."""

from typing import Sequence, Any, Union, Optional


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Return the first element of a sequence safely.

    Args:
        lst: A sequence of elements of any type

    Returns:
        The first element of the sequence if it exists, None otherwise
    """
    if lst:
        return lst[0]
    else:
        return None