#!/usr/bin/env python3
"""
module has responsible to detect element type.
"""
from typing import Mapping, Any, Union, Optional, TypeVar

T = TypeVar("T")


def safely_get_value(
    dct: Mapping[Any, Any], key: Any, default: Optional[Union[T, None]] = None
) -> Union[Any, T]:
    """
    Retrieve a value from a dictionary safely.

    Args:
        dct (Mapping[Any, Any]): The dictionary from which to retrieve value.
        key (Any): The key for the value to retrieve.
        default (Optional[Union[T, None]]): The default value to return key
        is not in the dictionary.

    Returns:
        Union[Any, T]: The value associated with the key in , or the
        default value if the key is not found.
    """
    if key in dct:
        return dct[key]
    else:
        return default
