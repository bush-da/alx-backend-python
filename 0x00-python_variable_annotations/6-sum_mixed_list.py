#!/usr/bin/env python3
"""Function which takes a list of integer and floats and returns their sum"""
from typing import List, Union

def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """Returns the sum of mixed float and integer numbers"""
    return sum(mxd_list)
