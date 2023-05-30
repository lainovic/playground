class LRUCache:
    class Node:
        def __init__(self, key=None, val=None):
            self.key = key
            self.val = val
            self.prv = self.nxt = None

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = self.Node()  # <- least recent
        self.tail = self.Node()  # <- most recent
        self.head.nxt = self.tail
        self.tail.prv = self.head

    def peek(self) -> int:
        print("---> peek() called.")
        if len(self.cache) == 0:
            return None
        return self.tail.prv.val

    def get(self, key: int) -> int:
        print(f"---> get({key}) called.")
        if len(self.cache) == 0:
            return -1
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._remove(node)
        self._append(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        print(f"---> put({key}, {value}) called.")
        if key in self.cache:
            self._update(key, value)
        else:
            self._add(key, value)

    def _add(self, key, value):
        print(f"---> _add({key}, {value}) called.")
        node = self.Node(key=key, val=value)
        self.cache[key] = node
        if len(self.cache) > self.capacity:
            self._prune()
        self._append(node)

    def _update(self, key, value):
        print(f"---> _update({key}, {value}) called.")
        node = self.cache[key]
        node.val = value
        self._remove(node)
        self._append(node)

    def _remove(self, node):
        print("---> _remove() called.")
        prv, nxt = node.prv, node.nxt
        prv.nxt, nxt.prv = nxt, prv

    def _append(self, node):
        print("---> _append() called.")
        prv, nxt = self.tail.prv, self.tail
        prv.nxt, node.prv = node, prv
        node.nxt, nxt.prv = nxt, node

    def _prune(self):
        key = self.head.nxt.key
        val = self.head.nxt.val
        print(f"---> _prune(): ({key}, {val}) pruned.")
        del self.cache[key]
        self._remove(self.head.nxt)
        return key


if __name__ == "__main__":
    capacity = 3
    cache = LRUCache(capacity)
    cache.put(1, 1)
    cache.put(2, 2)
    print(cache.peek())
    print(cache.get(1))
    print(cache.peek())
    cache.put(3, 3)
    print(cache.peek())
    print(cache.get(3))
    print(cache.peek())
    cache.put(4, 4)
    print(cache.peek())
    print(cache.get(2))
    print(cache.peek())
    print(cache.get(1))
    print(cache.peek())
    print("Done!")
