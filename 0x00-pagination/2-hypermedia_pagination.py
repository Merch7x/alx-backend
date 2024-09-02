#!/usr/bin/env python3
"""Implement methods to paginate a dataset"""

import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def index_range(self, page: int, page_size: int):
        """return a tuple of size two containing \
          a start index and an end index corresponding\
          to the range of indexes to return in a list for\
          those particular pagination parameters.
        """
        start_index = (page - 1) * page_size
        end_index = start_index + page_size
        return start_index, end_index

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Gets a particular page"""
        if page <= 0 or not isinstance(page, int)\
                and page_size <= 0 or not isinstance(page_size, int):
            raise AssertionError
        else:
            dataset = self.dataset()
            index_range = self.index_range(page, page_size)
            return dataset[slice(*index_range)]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Returns a dictionary with pagination details."""

        total_items = len(self.dataset())
        total_pages = math.ceil(total_items / page_size)

        data = self.get_page(page, page_size)
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        return {
            'page_size': page_size,
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }
