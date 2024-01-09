#!/usr/bin/env python3
""""""


def index_range(page: int, page_size: int):
    """"""
    index_tuple = (((page * page_size) - page_size), page * page_size)
    return index_tuple
