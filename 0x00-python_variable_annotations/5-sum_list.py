#!/usr/bin/python3
"""
This module contains a function to sum a list of floats
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Sum a list of floats

    Args:
        input_list (list[float]): A list of floats

    Returns:
        float: The sum of the list of floats
    """
    sum: float = 0
    for number in input_list:
        sum += number

    return sum
