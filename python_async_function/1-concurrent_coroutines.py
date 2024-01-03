#!/usr/bin/env python3

""""""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    float_list = []
    for i in range(n):
        wait_time = wait_random(max_delay)
        await asyncio.sleep(wait_time)
        float_list.append(wait_time)
    return sorted(float_list)
