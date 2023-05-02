#!/usr/bin/env python3
"""
This module contains the function measure_runtime that measures the total
execution time for async_comprehension four times in parallel using
asyncio.gather
"""
import asyncio
import time
from typing import List, Coroutine

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Return the time it takes to execute async_comprehension
    four times in parallel

    Returns:
        float: time it takes to execute async_comprehension
               four times in parallel
    """
    start = time.time()

    coroutines: List[Coroutine] = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*coroutines)

    return time.time() - start
