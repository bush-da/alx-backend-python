#!/usr/bin/env python3
"""function with integers n and max_delay as arguments that measures
 the total execution time for wait_n(n, max_delay),
and returns total_time / n. Your function should return a float."""
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """Function that measure the total execution time for
    wait_n(n, max_delay) and
    Return:
          total_time / n
    """
    start_time = time.perf_counter()

    await wait_n(n, max_delay)

    end_time = time.perf_counter()

    total = end_time - start_time

    return total / n
