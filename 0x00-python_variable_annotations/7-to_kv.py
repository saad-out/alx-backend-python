#!/usr/bin/env python3
"""
This module contains a function to return a tuple of a string and a float
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple of a string and a float

    Args:
        k (str): A string
        v (Union[int, float]): A number

    Returns:
        Tuple[str, float]: A tuple of a string and a float
    """
    return (k, float(v * v))
