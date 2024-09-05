#!/usr/bin/env python3
"""Implemenys LFU caching"""
from base_caching import BaseCaching
from collections import OrderedDict


class LFUCache(BaseCaching):
    """Implements a Last Recently Used caching
       mechanism
    """

    def __init__(self):
        """Initialize an object"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return
        elif key in self.cache_data:
            self.cache_data.move_to_end(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            k, v = self.cache_data.popitem(last=False)
            print(f'DISCARD: {k}')

        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        else:
            self.cache_data.move_to_end(key)
        return self.cache_data.get(key)
