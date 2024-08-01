#!/usr/bin/env python3
"""
module to make sum lists of floats.
"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Calculate the sum of a list of floats.

    Args:
        input_list: A list of floats.

    Returns:
        The sum of all floats in the list.
    """
    return float(sum(input_list))
