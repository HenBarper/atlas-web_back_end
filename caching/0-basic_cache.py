#!/usr/bin/python3
"""Create a class BasicCache that
inherits from BaseCaching and
is a caching system:"""
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
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        else:
            return None
