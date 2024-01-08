#!/usr/bin/python3
""""""
BaseCaching = __import__('base_caching').BaseCaching

class BasicCache(BaseCaching):
    """Basic cache class"""

    def put(self, key, item):
        """Put function of basic cache"""
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """Get function of basic cache"""
        if key is not None:
            return self.cache_data[key]
        else:
            return None