#!/usr/bin/env python3
"""
This module contains the function element_length which takes an iterable
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples containing the elements of lst and their lengths

    Args:
        lst (Iterable[Sequence]): A list of elements

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples containing the elements
    """
    return [(i, len(i)) for i in lst]
