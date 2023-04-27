#!/usr/bin/env python3
"""
This module contains a function that returns a function that
multiplies a float by multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by multiplier

    Args:
        multiplier (float): A float number

    Returns:
        Callable[[float], float]: A function that multiplies
                                a float by multiplier
    """
    def multiply_by_multiplier(number: float) -> float:
        """
        Multiplies a float by multiplier

        Args:
            number (float): A float number

        Returns:
            float: The product of multiplier and number
        """
        return float(multiplier * number)

    return multiply_by_multiplier
