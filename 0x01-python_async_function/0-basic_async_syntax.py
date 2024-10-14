#!/usr/bin/env python3
"""create a coroutine that takes argument and
delay according to the argument"""
import random
import asyncio


async def wait_random(max_delay=10):
    """generate random number b/n 0 and max_delay and
    sleep for number b/n max_delay and 0 and return time taken"""
    max_delay = random.randint(0, max_delay) * random.random()
    await asyncio.sleep(max_delay)
    return max_delay
