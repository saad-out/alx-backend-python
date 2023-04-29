#!/usr/bin/env python3
"""
This module contains the function wait_n that takes
an integer n and max_delay and returns the list of all
the delays (float values).
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Return the list of all the delays (float values). The list of the
    delays should be in ascending order without using sort() because of
    concurrency.

    Args:
        n (int): number of times wait_random will be called
        max_delay (int): max random delay

    Returns:
        List[float]: list of all the delays
    """
    tasks: List[asyncio.Task]
    tasks = [task_wait_random(max_delay) for _ in range(n)]

    results: List[float] = []
    for coroutine in asyncio.as_completed(tasks):
        result: float = await coroutine
        results.append(result)

    return results
