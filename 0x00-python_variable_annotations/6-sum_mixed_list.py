#!/usr/bin/env python3
"""
Module to sum a list of integers and floats.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Sums a list of integers and floats.

    Args:
        mxd_lst (List[Union[int, float]]): A list containing integers floats.

    Returns:
        float: The sum of the integers and floats in the list.
    """
    return float(sum(mxd_lst))
