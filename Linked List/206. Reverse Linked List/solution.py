# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        nodes = []
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next
            
        node = nodes.pop()
        result = node
        curr = result
        while nodes:
            node = nodes.pop()
            curr.next = node
            curr = node
        
        curr.next = None
        
        return result
    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        
        def helper(node) -> (Optional[ListNode], Optional[ListNode]):
            if node.next is None:
                return node, node
            h, t = helper(node.next)
            t.next = node
            return h, node
        
        result, tail = helper(head)
        head.next = None
        return result
        
