class DListNode(object):
    def __init__(self, pre, next, key, value):
        self.key, self.value = key, value
        self.pre = pre
        self.next = next


def printL(r):
    s = ''
    while r is not None:
        s += (str(r.key) + ' -> ')
        r = r.next
    print(s)


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.c = capacity
        self.cache = {}
        self.head = DListNode(None, None, 0, 0)
        self.tail = DListNode(self.head, None, 0, 0)
        self.head.next = self.tail

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache:
            return -1
        self.move_to_head(key)
        return self.cache[key].value

    def move_to_head(self, key):
        current_node = self.cache[key]
        current_node.pre.next = current_node.next
        current_node.next.pre = current_node.pre
        self.tail.pre.next, current_node.pre = current_node, self.tail.pre
        self.tail.pre, current_node.next = current_node, self.tail

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            self.move_to_head(key)
            self.cache[key].value = value
        else:
            current_node = DListNode(self.tail.pre, self.tail, key, value)
            self.tail.pre.next, self.tail.pre = current_node, current_node
            self.cache[key] = current_node
            if len(self.cache) > self.c:
                self.cache.pop(self.head.next.key)
                self.head.next = self.head.next.next
                self.head.next.pre = self.head


if __name__ == '__main__':
    lRUCache = LRUCache(2)
    lRUCache.put(1, 1)
    lRUCache.put(2, 2)
    printL(lRUCache.head)
    print(lRUCache.get(1))
    printL(lRUCache.head)
    lRUCache.put(3, 3)
    print(lRUCache.get(2))
    lRUCache.put(4, 4)
    print(lRUCache.get(1))
    print(lRUCache.get(3))
    print(lRUCache.get(4))
