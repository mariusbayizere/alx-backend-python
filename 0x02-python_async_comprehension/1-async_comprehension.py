#!/usr/bin/env python3
"""
This module contains a coroutine that from an asynchronous generator.
"""

from typing import List

async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """
    Collects random numbers from an asynchronous generator.

    This coroutine collects 10 random numbers from the async_generator
    and returns them as a list.

    Returns:
        List[float]: A list of random numbers collected from async generator.
    """
    v = [x async for x in async_generator()]
    return v
