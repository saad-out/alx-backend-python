#!/usr/bin/env python3
"""
This module contains a function to return the value of a key in a dictionary
"""
from typing import Union, Any, TypeVar, Mapping


T = TypeVar('T')


def safely_get_value(dct: Mapping,
                     key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
    Return the value of a key in a dictionary if it exists, otherwise return

    Args:
        dct (Mapping): A dictionary
        key (Any): A key
        default (Union[T, None], optional): A default value. Defaults to None.

    Returns:
        Union[Any, T]: The value of a key in a dictionary if it exists,
    """
    if key in dct:
        return dct[key]
    else:
        return default
