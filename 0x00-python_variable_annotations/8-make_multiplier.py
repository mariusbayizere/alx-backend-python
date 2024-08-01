#!/usr/bin/env python3
"""
Module that has responsile to make multiplication.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create a function that multiplies a given value by a specified multiplier.

    Args:
        multiplier (float): The base number to multiply by.

    Returns:
        Callable[[float], float]: A function that takes a float and returns the
        product of it and the multiplier.
    """
    return lambda x: multiplier * x
