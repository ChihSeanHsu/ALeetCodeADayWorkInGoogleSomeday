# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# we can use hash map to solve this problem, but there is a condition to usse constant memory.

# use slow(move one node a time) and fast(move two node a time) pointer, they will meet if there is a loop.
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        
        return False
