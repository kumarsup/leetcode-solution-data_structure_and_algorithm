class LitsNode:
    def __initi__(self):
        self.key = 0
        self.value = 0
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.size = 0
        self.head = LitsNode()
        self.tail = LitsNode()

        self.head.next = self.tail
        self.tail.prev = self.head

    def put(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.move_to_head(node)
        else:
            node = ListNode()
            node.key = key
            node.value = value
            self.add_node(node)
            self.cache[key] = node
            self.size += 1

            if self.size > self.capacity:
                tail = self.pop_tail()
                del self.cache[tail.key]
                self.size -= 1

    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self.move_to_head(node)
            return node.value
        return -1

    def move_to_head(self, node):
        self.remove_node(node)
        self.add_node(node)

    def remove_node(self, node):
        prev = node.prev
        new = node.next

        prev.next = new
        new.prev = prev

    def add_node(self, node):
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

    def pop_tail(self):
        node = self.tail.prev
        self.remove_node(node)
        return node