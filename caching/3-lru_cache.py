#!/usr/bin/python3
"""Create a class LRUCache that
inherits from BaseCaching and
is a caching system:"""
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """LRU cache class"""
    def __init__(self):
        """LRU Cache  init method"""
        super().__init__()

    def put(self, key, item):
        """Put function of basic cache"""
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discarded_key = max(self.cache_data, key=lambda k: self.cache_data[k])
                print(f"DISCARD: {discarded_key}")
                del self.cache_data[discarded_key]
            self.cache_data[key] = item

    def get(self, key):
        """Get function of basic cache"""
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        else:
            return None
