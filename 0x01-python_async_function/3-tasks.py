#!/usr/bin/env python3
"""
Python Async Task Creation Module
"""
import asyncio
wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create an asynchronous task to wait for a random delay.

    Args:
        max_delay (int): Maximum delay time in seconds.

    Returns:
        asyncio.Task: An asynchronous task that waits for a random delay.
    """
    return asyncio.create_task(wait_random(max_delay))
