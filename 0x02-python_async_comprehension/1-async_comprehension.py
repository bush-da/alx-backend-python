#!/usr/bin/env python3
"""Async Comprehension function"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Collects 10 random numbers from async_generator."""
    return [number async for number in async_generator()]
