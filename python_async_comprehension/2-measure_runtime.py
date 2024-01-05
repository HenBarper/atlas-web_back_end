#!/usr/bin/env python3

"""Import async_comprehension from the previous
file and write a measure_runtime coroutine that
will execute async_comprehension four times in
parallel using asyncio.gather."""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """measure_runtime should measure
    the total runtime and return it."""
    start_time: float = time.time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension())
    end_time: float = time.time()
    return end_time - start_time
