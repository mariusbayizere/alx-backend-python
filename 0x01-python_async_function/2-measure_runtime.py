#!/usr/bin/env python3
"""
Measure the Execution Time of an Asynchronous Function
"""
import time
from asyncio import run

wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time average time per call.

    Args:
        n (int): The number of times to call the `wait_n` coroutine.
        max_delay (int): The maximum delay parameter to pass to `wait_n`.

    Returns:
        float: The total time taken to execute the number of calls (n).
    """
    U: float = time.perf_counter()
    run(wait_n(n, max_delay))
    K: float = time.perf_counter()
    Result: float = K - U
    return Result
