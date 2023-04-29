#!/usr/bin/env python3
"""
This module contains the function measure_time that measures
the total execution time for wait_n(n, max_delay), and returns
total_time / n.
"""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the runtime of wait_n

    Args:
        n (int): number of times wait_random will be called
        max_delay (int): max random delay

    Returns:
        float: average runtime
    """
    start: float = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end: float = time.perf_counter()

    return (end - start) / n
