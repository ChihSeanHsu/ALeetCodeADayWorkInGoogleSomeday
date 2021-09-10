# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        depth = 1
        queue = deque([root])
        
        while queue:
            n = len(queue)
            for _ in range(n):
                node = queue.popleft()
                if node.right is None and node.left is None:
                    return depth
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
                    
            depth += 1
        
        return depth
            
                
