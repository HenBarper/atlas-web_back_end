#!/usr/bin/env python3

"""Write a type-annotated function make_multiplier
that takes a float multiplier as argument"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that
    multiplies a float by multiplier."""
    def multiply_it(num: float) -> float:
        return num * multiplier
    return multiply_it
