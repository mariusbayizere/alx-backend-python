#!/usr/bin/env python3
"""
This module contains an asynchronous generator that yields random numbers.
"""

import asyncio
from typing import Generator
import random


async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronously generates random numbers.

    This coroutine loops 10 times, each time waiting asynchronously second,
    then yielding a random float between 0 and 10.

    Yields:
        float: A random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
