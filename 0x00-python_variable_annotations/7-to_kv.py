#!/usr/bin/env python3
"""
Module that has responsible to make data.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Convert a key and value to a tuple with the value squared.

    Args:
        k (str): The key as a string.
        v (Union[int, float]): The value as an integer or float.

    Returns:
        Tuple[str, float]: A tuple where the first element.
    """
    return k, float(v ** 2)
