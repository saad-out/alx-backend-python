#!/usr/bin/env python3
"""
This module contains the function async_generator that takes no arguments and
returns a generator object that will yield a random number between 0 and 10
"""
import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Return a generator of random numbers between 0 and 10

    Yields:
        Generator[float, None, None]: [description]
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
