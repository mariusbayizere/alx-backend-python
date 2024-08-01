#!/usr/bin/env python3
"""
Module for safely retrieving a value from a dictionary with optional default value.
"""
from typing import Mapping, Any, Optional, TypeVar

T = TypeVar('T')

def safely_get_value(
    dct: Mapping[Any, Any], 
    key: Any, 
    default: Optional[T] = None
) -> Optional[T]:
    """
    Retrieves the value from a dictionary if the key exists.

    Args:
        dct (Mapping[Any, Any]): The dictionary to search in.
        key (Any): The key to look for in the dictionary.
        default (Optional[T], optional): The default value to return.

    Returns:
        Optional[T]: The value associated with the key if it exists.
    """
    if key in dct:
        return dct[key]
    else:
        return default
