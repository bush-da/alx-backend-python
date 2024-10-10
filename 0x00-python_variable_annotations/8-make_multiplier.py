#!/usr/bin/env python3
"""Function that takes a float multiplier as argument and
   returns a function that multiplies a float by multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return function that multiply by multiplier variable value"""
    def ret(x: float) -> float:
        return multiplier * x
    return ret
