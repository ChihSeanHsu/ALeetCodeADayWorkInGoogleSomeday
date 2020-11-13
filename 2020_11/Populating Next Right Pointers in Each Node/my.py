"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None or root.left is None:
            return root
        queue = deque()
        queue.append(root.left)
        queue.append(root.right)
        head = root.left
        node_count = 2
        current_count = 0
        while len(queue) > 0:
            current_count += 1
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
                queue.append(node.right)
            
            if current_count == 1:
                head = node
            else:
                head.next = node
                head = node
            
            if current_count == node_count:
                current_count = 0
                node_count *= 2
                
        return root
        
