#!/usr/bin/env python3

"""Create a measure_time function with integers
n and max_delay as arguments that measures the
total execution time for wait_n(n, max_delay),
and returns total_time / n. Your function should
return a float."""
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Use the time module to measure
    an approximate elapsed time."""
    start_time: float = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time: float = time.time()
    total_time: float = end_time - start_time
    return total_time / n
