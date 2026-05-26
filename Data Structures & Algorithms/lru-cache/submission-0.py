class Nodes:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):

        self.cap = capacity
        self.cache = {}

        self.left = Nodes(0,0)
        self.right = Nodes(0,0)

        self.left.next = self.right
        self.right.prev = self.left

    def remove(self,node):
        prev_node = node.prev
        nxt_node = node.next
        
        prev_node.next = nxt_node
        nxt_node.prev = prev_node

    def insert(self, node):
        prev_node = self.right.prev
        nxt_node = self.right
        
        prev_node.next = node
        nxt_node.prev = node
        
        node.next = nxt_node
        node.prev = prev_node

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val

        return -1

    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            self.remove(self.cache[key])
            
        self.cache[key] = Nodes(key, value)
        self.insert(self.cache[key])
        
        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        
