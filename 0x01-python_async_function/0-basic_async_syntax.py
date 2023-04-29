#!/usr/bin/env python3
"""
This module contains the function wait_random that takes
an integer max_delayand waits for a random delay between
0 and max_delay
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Waits for a random delay between 0 and max_delay

    Args:
        max_delay (int, optional): max random delay. Defaults to 10.

    Returns:
        sleep_time (float): random delay
    """
    sleep_time: float = random.uniform(0, max_delay)
    await asyncio.sleep(sleep_time)
    return sleep_time
