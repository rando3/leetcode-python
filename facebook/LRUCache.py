class ListNode:
    def __init__(self, key, value, next=None, prev=None):
        self.key = key
        self.val = value
        self.next = next
        self.prev = prev


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self._map = {}
        self._head = ListNode(0, 0)
        self._tail = ListNode(0, 0)
        self._head.next = self._tail
        self._tail.prev = self._head

    def get(self, key):
        if key in self._map:
            node = self._map[key]
            self._remove(node)
            self._add(node)
            return node.val
        return -1

    def put(self, key, value):
        if key in self._map:
            self._remove(self._map[key])
        node = ListNode(key, value)
        self._add(node)
        self._map[key] = node
        if len(self._map) > self.capacity:
            node = self._head.next
            self._remove(node)
            del self._map[node.key]

    def _remove(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def _add(self, node):
        prev = self._tail.prev
        prev.next = node
        node.prev = prev
        node.next = self._tail
        self._tail.prev = node


''' OR '''
import collections


class LRUCache2:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.dict = collections.OrderedDict()
        self.capacity = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.dict:
            return -1
        self.dict.move_to_end(key)
        return self.dict[key]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.dict:
            del self.dict[key]
        else:
            if len(self.dict) >= self.capacity:
                self.dict.popitem(last=False)
        self.dict[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

if __name__ == "__main__":
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print(cache.get(1))      # returns 1
    cache.put(3, 3)   # evicts key 2
    print(cache.get(2))      # returns -1 (not found)
    cache.put(4, 4)   # evicts key 1
    print(cache.get(1))    # returns -1 (not found)
    print(cache.get(3))     # returns 3
    print(cache.get(4))     # returns 4
