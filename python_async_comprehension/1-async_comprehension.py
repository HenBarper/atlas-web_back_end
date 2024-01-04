#!/usr/bin/env python3

"""Import async_generator from the previous
task and then write a coroutine called
async_comprehension that takes no arguments."""
import random
import asyncio
import typing
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> typing.List[float]:
    """The coroutine will collect10 random numbers
    using an async comprehensing over async_generator,
    then return the 10 random numbers."""
    rand_nums = []
    for i in range(10):
        rand_nums.append(random.uniform(0, 10))
    return rand_nums
