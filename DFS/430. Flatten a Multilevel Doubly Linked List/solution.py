"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if head is None:
            return
        def helper(node):
            while node.next or node.child:
                if node.child:
                    tail = helper(node.child)
                    tail.next = node.next
                    if node.next:
                        node.next.prev = tail
                    node.child.prev = node
                    node.next = node.child
                    node.child = None
                node = node.next
            return node
        helper(head)
        return head
      
      
      
      
    def flatten(self, head: 'Node') -> 'Node':
        if head is None:
            return 

        stack = [head]
        prev = None
        while stack:
            node = stack.pop()
            if node.next:
                stack.append(node.next)
            if node.child:
                stack.append(node.child)
            node.prev = prev
            node.next = stack[-1] if stack else None
            node.child = None
            prev = node
        
        return head
            
            
                
            
