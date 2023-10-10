#!/usr/bin/env python3
"""
a coroutine called async_generator that takes no arguments.
"""
import asyncio
import time
async_com = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """coroutine that will execute async_comprehension four times in
    parallel using asyncio.gather, measures the total runtime and
    return it"""
    start: float = time.time()
    await asyncio.gather(async_com(), async_com(), async_com(),
                         async_com())
    end: float = time.time()

    total_runtime = end - start
    return total_runtime
