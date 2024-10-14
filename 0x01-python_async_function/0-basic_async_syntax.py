#!/usr/bin/env python3
"""create a coroutine that takes argument and
delay according to the argument"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """generate random number b/n 0 and max_delay and
    sleep for number b/n max_delay and 0 and return time taken"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
