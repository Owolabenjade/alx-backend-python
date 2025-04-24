#!/usr/bin/env python3
"""Module for calculating the length of elements in an iterable sequence."""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return a list of tuples containing elements and their lengths.

    Args:
        lst: An iterable of sequences

    Returns:
        A list of tuples where each tuple contains a sequence from the
        input and its length
    """
    return [(i, len(i)) for i in lst]