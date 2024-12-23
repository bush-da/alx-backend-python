#!/usr/bin/env python3
"""Function that returns the first element or none"""
from typing import Sequence, Union, Any


# The types of the elements of the input are not know
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Return the first element or None"""
    if lst:
        return lst[0]
    else:
        return None
