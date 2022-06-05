from collections import OrderedDict

"""
Ordered
"""

class FirstUnique:

    def __init__(self, nums: List[int]):
        self.queue = OrderedDict()
        self.is_unique = {}
        for num in nums:
            self.add(num)

    def showFirstUnique(self) -> int:
        if self.queue:
            return next(iter(self.queue))
        return -1

    def add(self, value: int) -> None:
        if value not in self.is_unique:
            self.queue[value] = True
            self.is_unique[value] = True
        elif self.is_unique[value]:
            del self.queue[value]
            self.is_unique[value] = False

            
"""
LinkedList

"""
class ListNode:
    def __init__(self, key=0, prev=None, next=None):
        self.key = key
        self.prev = prev
        self.next = next
        
          
class FirstUnique:

    def _add_to_tail(self, node):
        node.next = self.tail
        node.prev = self.tail.prev
        self.tail.prev.next = node
        self.tail.prev = node
        
    def _remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = None
        node.next = None
        
    def __init__(self, nums: List[int]):
        self.seen = {}
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        
        for num in nums:
            self.add(num)

    def showFirstUnique(self) -> int:
        if self.head.next != self.tail:
            return self.head.next.key
        return -1

    def add(self, value: int) -> None:
        if value not in self.seen:
            node = ListNode(value)
            self._add_to_tail(node)
            self.seen[value] = node
        elif self.seen[value]:
            node = self.seen[value]
            self.seen[value] = None
            self._remove_node(node)


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
