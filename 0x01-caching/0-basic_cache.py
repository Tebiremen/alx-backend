#!/usr/bin/env python3
'''Basic dictionary module.
'''
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    '''Represents an object that allows storing and
    collecting items from a dictionary.
    '''
    def put(self, key, item):
        '''Added an item in the cache.
        '''
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        '''Collects an item by key.
        '''
        return self.cache_data.get(key, None)
