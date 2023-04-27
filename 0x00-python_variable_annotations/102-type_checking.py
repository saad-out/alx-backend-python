#!/usr/bin/env python3
"""
This module contains a type-annotated function zoom_array that takes a tuple
and returns a list
"""
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Returns a list of tuples containing the elements of lst and their lengths

    Args:
        lst (Tuple): A tuple of elements
        factor (int, optional): The factor by which to zoom the elements.
        Defaults to 2.

    Returns:
        List: A list of tuples containing the elements
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)
zoom_3x = zoom_array(array, int(3.0))
