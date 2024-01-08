#!/usr/bin/python3
""""""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """"""
    def __init__(self):
        """"""
        super().__init__()

    def put(self, key, item):
        """Put function of basic cache"""
        if key is None or item is None:
            pass
        elif len(self.cache_data) > BaseCaching.MAX_ITEMS:
            print(f"DISCARD: {self.cache_data[0].key}")
            self.cache_data[0]
        else:
            self.cache_data[key] = item

    def get(self, key):
        """Get function of basic cache"""
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        else:
            return None
