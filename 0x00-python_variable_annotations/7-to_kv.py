#!/usr/bin/env python3
"""Function that takes string k and float or int v as argument
   Returns a tuple"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return tuple first element string k and second elemen square
    of the int/float"""
    return tuple((k, v**2))
