#!/usr/bin/env python3

"""Write a type-annotated function sum_list which
takes a list input_list of floats as argument"""
import typing


def sum_list(input_list: typing.List[float]) -> float:
    """Returns their sum as a float"""
    sum = 0
    for item in input_list:
        sum += item
    return sum
