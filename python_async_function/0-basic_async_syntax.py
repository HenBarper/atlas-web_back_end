#!/usr/bin/env python3

"""asynchronous coroutine that takes in an integer argument"""
import asyncio
import random


async def wait_random(max_delay = 10):
    """waits for a random delay and eventually returns it"""
    wait_time = random.uniform(0, max_delay)
    await asyncio.sleep(wait_time)
    return wait_time