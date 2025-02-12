class Node:
    def __init__(self, k, v):
        self.next = None
        self.prev = None
        self.key = k
        self.val = v


class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.head = None
        self.tail = None
        self.cap = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        current = self.head
        while current is not None:
            if key == current.key:
                return current.val
            current = current.next
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        new_node = Node(key, value)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
