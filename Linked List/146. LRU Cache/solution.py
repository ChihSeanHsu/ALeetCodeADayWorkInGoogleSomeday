class ListNode:
    def __init__(self, key=0, value=0, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next


class LRUCache:

    def _remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        
    def _drop_head(self):
        self._remove_node(self.head.next)
        
    def _add_to_tail(self, node):
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node
    
    def _move_to_tail(self, node):
        self._remove_node(node)
        self._add_to_tail(node)

    def __init__(self, capacity: int):
        # key: node
        self.cache = {}
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._move_to_tail(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self._move_to_tail(node)
            node.value = value
            return
        else:
            # remove head
            if len(self.cache) >= self.capacity:
                del self.cache[self.head.next.key]
                self._drop_head()
                
            new_node = ListNode()
            new_node.key = key
            new_node.value = value
            self._add_to_tail(new_node)
            self.cache[key] = new_node

                

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
