#!/usr/bin/env python3
"""
Asynchronous Coroutine for Random Delay
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay.

    Args:
        max_delay (int): The maximum delay time in seconds. Default is 10.

    Returns:
        float: The actual delay time in seconds.
    """
    v: float = random.uniform(0, float(max_delay))
    await asyncio.sleep(v)
    return v
