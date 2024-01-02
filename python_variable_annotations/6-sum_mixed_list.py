#!/usr/bin/env python3

"""Write a type-annotated function sum_mixed_list
which takes a list mxd_lst of integers and floats"""
import typing


def sum_mixed_list(mxd_lst: typing.List[typing.Union[int, float]]) -> float:
    """Returns their sum as a float"""
    sum = 0
    for item in mxd_lst:
        sum += item
    return sum
