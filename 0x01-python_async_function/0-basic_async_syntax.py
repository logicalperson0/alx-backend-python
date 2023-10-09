#!/usr/bin/env python3
"""
an asynchronous coroutine file
"""
import asyncio
import random


async def wait_random(max_delay = 10) -> float:
    """asynchronous coroutine that takes in an integer argument (max_delay,
    with a default value of 10) named wait_random that waits for a random
    delay between 0 and max_delay"""
    flo_rand = random.uniform(0, max_delay)
    await asyncio.sleep(flo_rand)
    return flo_rand
