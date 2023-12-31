#!/usr/bin/env python3
"""
an asynchronous coroutine file
"""
import asyncio
from typing import List
waiting = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """return the list of all the delays (float values). The list of the
    delays should be in ascending order without using SORTING because
    of concurrency."""
    wait_x: List[float] = []
    total_wait: List[float] = []

    for x in range(n):
        wait_x.append(waiting(max_delay))

    for y in asyncio.as_completed(wait_x):
        zee = await y
        total_wait.append(zee)

    return total_wait
