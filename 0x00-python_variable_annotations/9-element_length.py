#!/usr/bin/env python3
"""Function return element length"""
from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns a list of tuples where each tuple contains
    an element and its length."""
    return [(i, len(i)) for i in lst]
