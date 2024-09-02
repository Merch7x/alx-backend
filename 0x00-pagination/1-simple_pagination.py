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
            start_index, end_index = self.index_range(page, page_size)
            if start_index >= len(dataset):
                return []

            return dataset[start_index:end_index]
