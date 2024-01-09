#!/usr/bin/env python3
"""Implement a method named get_page
that takes two integer arguments page
with default value 1 and page_size with
default value 10."""

import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of
    popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        pass

    def index_range(self, page: int, page_size: int):
        """The function should return a tuple
        of size two containing a start index
        and an end index corresponding to the
        range of indexes to return in a list
        for those particular pagination parameters."""
        index_tuple = (((page * page_size) - page_size), page * page_size)
        return index_tuple

    def get_page(self, page: int = 1, page_size: int = 10):
        """Use index_range to find the correct indexes
        to paginate the dataset correctly and return
        the appropriate page of the dataset (i.e. the
        correct list of rows)."""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start_index, end_index = self.index_range(page, page_size)
        dataset = self.dataset()

        if start_index >= len(dataset):
            return []

        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10):
        """Implement a get_hyper method that takes the
        same arguments (and defaults) as get_page and
        returns a dictionary containing the following
        key-value pairs:"""
        dataset = self.dataset()
        total_pages = page_size * page

        if page + 1 > total_pages:
            next_page = None
        else:
            next_page = page + 1

        if page - 1 > 1:
            prev_page = None
        else:
            prev_page = page - 1

        hyper_dict = {
            'page_size': page_size,
            'page': page,
            'data': self.get_page(page, page_size),
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }
        return hyper_dict
