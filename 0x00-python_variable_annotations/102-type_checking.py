#!/usr/bin/env python3
"""
Module to zoom into elements of a tuple.
"""
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Create a zoomed-in list from the elements of a tuple by repeating element.

    Args:
        lst (Tuple): The tuple containing elements to zoom into.
        factor (int): The factor by which to zoom into the elements. is 2.

    Returns:
        List: A list containing the zoomed-in elements.
    """
    zoomed_in: List = [item for item in lst for i in range(factor)]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
