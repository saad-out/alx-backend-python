#!/usr/bin/env python3
"""
This module contains a function to sum a list of floats or integers
"""
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Sum a list of floats or integers

    Args:
        mxd_lst (list[Union[int, float]]): A list of floats or integers

    Returns:
        float: The sum of the list of floats or integers
    """
    sum: float = 0
    for number in mxd_lst:
        sum += number

    return sum
