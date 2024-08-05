#!/usr/bin/env python3
"""
Asynchronous Coroutine for Multiple Random Delays
"""
from asyncio import gather
from typing import List


wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous coroutine that spawns `wait_random` times specify `max_delay`.

    Args:
        n (int): The number of times to call `wait_random`.
        max_delay (int): The maximum delay time for each call to `wait_random`.

    Returns:
        List[float]: A list of delays (floats) in ascending order.
    """
    v: List[callable] = [wait_random(max_delay) for _ in range(n)]
    S: List[float] = await gather(*v)
    return sorted(S)
