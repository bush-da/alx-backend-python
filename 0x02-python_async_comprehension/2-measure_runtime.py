#!/usr/bin/env python3
"""Measure the total runtime for executing async_comprehension 4 times in parallel"""
import asyncio
import time
async_comprehension =  __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measure total runtime for running async_comprehension four times in parallel."""
    start_time = time.perf_counter()

    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())

    end_time = time.perf_counter()

    total_runtime = end_time - start_time

    return total_runtime
