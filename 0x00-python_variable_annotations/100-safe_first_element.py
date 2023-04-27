#!/usr/bin/env python3
"""
This module contains a function to return the first element of a list
"""
from typing import Union, Sequence, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Return the first element of lst if there is any, otherwise None

    Args:
        lst (Sequence[Any]): A list of any type

    Returns:
        Union[Any, None]: The first element of lst if there is any,
                         otherwise None
    """
    if lst:
        return lst[0]
    else:
        return None
