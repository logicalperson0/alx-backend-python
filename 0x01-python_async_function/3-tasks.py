#!/usr/bin/env python3
"""
an asynchronous coroutine file
"""
import asyncio
wait = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """task_wait_random that takes an integer max_delay and returns
    a asyncio.Task"""
    create = asyncio.create_task(wait(max_delay))

    return create
