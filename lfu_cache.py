from lru_cache import LRUCache
from prio_queue import PriorityQueue


class LFUCache:
    class Node:
        def __init__(self, key, value, usage_counter):
            self.key = key
            self.val = value
            self.counter = usage_counter

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = LRUCache(capacity)
        self.counters = {}

    def get(self, key):
        ...

    def put(self, key, val):
        if key in self.cache:
            node = self.cache[key]
            node.val = val
            node.counter += 1
            return
        node = self.Node(key, val, 1)
        self.cache.put(key, node)
        if self.cache.size <= self.capacity:
            return
        print("---> capacity exceeded")
