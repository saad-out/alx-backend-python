#!/usr/bin/env python3
"""
This module contains the function async_comprehension that takes no arguments
and returns a list of random numbers between 0 and 10
"""
import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Return a list of random numbers between 0 and 10

    Returns:
        List[float]: [description]
    """
    return [number async for number in async_generator()]
