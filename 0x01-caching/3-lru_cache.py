#!/usr/bin/env python3
"""Implemenys LRU caching"""
from base_caching import BaseCaching
from functools import lru_cache


class LRUCache(BaseCaching):
    """Implements a Last Recently Used caching
       mechanism
    """

    def __init__(self):
        """Initialize an object"""
        super().__init__()

    # @lru_cache(maxsize=BaseCaching.MAX_ITEMS)
    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return

        while len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            k = next(iter(self.cache_data))
            self.cache_data.pop(k)
            print(f'DISCARD: {k}')

        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if key is None:
            return None
        return self.cache_data.get(key)
