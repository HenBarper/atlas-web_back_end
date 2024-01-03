#!/usr/bin/env python3

""""""
import asyncio
import random
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> float:
    float_list = []
    wait_time: float = 0
    for i in range(n):
        wait_time = random.uniform(0, max_delay)
        await asyncio.sleep(wait_time)
        float_list.append(wait_time)
    return float_list
