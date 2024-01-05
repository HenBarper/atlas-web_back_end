#!/usr/bin/env python3

""""""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """"""
    start_time: float = time.time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension())
    end_time: float = time.time()
    return end_time - start_time
