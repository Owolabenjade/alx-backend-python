#!/usr/bin/env python3
"""Module for creating a function that multiplies a float by a multiplier."""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Create a function that multiplies a float by a given multiplier.

    Args:
        multiplier: The float value to multiply by

    Returns:
        A function that takes a float and returns the product of
        the float and the multiplier
    """
    def multiply(n: float) -> float:
        """Multiply a number by the stored multiplier.

        Args:
            n: The float to be multiplied

        Returns:
            The product of n and the stored multiplier
        """
        return n * multiplier

    return multiply