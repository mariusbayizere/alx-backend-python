#!/usr/bin/env python3
"""
This module contain to measure the runtime of executing async comprehensions.
"""

import time
import asyncio

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """
    Measures the total runtime of executing async comprehensions.

    This coroutine executes async_comprehension four concurrently and measures
    the total runtime.

    Returns:
        float: The total runtime in seconds.
    """
    v = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    xx = time.perf_counter() - v

    return xx
