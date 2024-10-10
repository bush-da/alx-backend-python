#!/usr/bin/env python3
"""Function that returns a value from the dictionary based on the key."""
from typing import Mapping, Any, Union, TypeVar


T = TypeVar('T')  # TypeVar for the default value type


def safely_get_value(
    dct: Mapping, key: Any, default: Union[T, None] = None
) -> Union[Any, T]:
    """Returns the value from the dictionary for the given key,
    or the default."""
    if key in dct:
        return dct[key]
    else:
        return default
