class Node:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.l = Node()
        self.r = Node()
        self.l.next = self.r
        self.r.prev = self.l

    # insert node at right
    def insert(self, node):
        temp = self.r.prev
        self.r.prev = node
        node.prev = temp
        node.next = self.r
        node.prev.next = node

    def remove(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next
        return node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        if len(self.cache) > self.capacity:
            lru = self.l.next
            self.remove(lru)
            del self.cache[lru.key]
        self.insert(self.cache[key])