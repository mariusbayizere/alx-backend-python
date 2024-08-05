#!/usr/bin/env python3
"""
Python Async Task Management Module
"""
from asyncio import gather
from typing import List

task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Execute multiple asynchronous tasks, each waiting random delay.

    Args:
        n (int): Number of tasks to create.
        max_delay (int): Maximum delay time in seconds for task.

    Returns:
        List[float]: A sorted list of delays from the complete.
    """
    call: List[callable[[int], float]] = [
        task_wait_random(max_delay) for _ in range(n)
    ]
    R: List[float] = await gather(*call)
    return sorted(R)
