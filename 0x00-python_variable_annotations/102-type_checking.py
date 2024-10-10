#!/usr/bin/env python3
"""Function that double or triple or more elements of tuple
   based on passed factor number"""
from typing import Tuple, Any, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Return tuple elements based on passed factor"""
    zoomed_in: List = [
        item for item in lst
        for i in range(int(factor))
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
