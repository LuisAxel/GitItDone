class ListNode:
    def __init__(self, key = 0, val = 0, prev = None, next = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.total = 0
        self.nodes = {}
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.nodes:
            return -1

        node = self.evict(key)
        self.add(node.key, node.val)
        return node.val

    def put(self, key: int, val: int) -> None:
        if key in self.nodes:
            self.evict(key)
        else:
            self.total += 1

        self.add(key, val)

        if self.total > self.capacity:
            self.evict(self.head.next.key)
            self.total -= 1

    def evict(self, key: int) -> ListNode:
        node = self.nodes[key]
        del self.nodes[key]

        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = None
        node.prev = None
        return node

    def add(self, key: int, val: int) -> None:
        node = ListNode(key, val, self.tail.prev, self.tail)
        self.nodes[key] = node

        self.tail.prev.next = node
        self.tail.prev = node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
