import heapq
from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        heap = []
        curr = root
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node:
                heapq.heappush(heap, node.val)
                queue.append(node.left)
                queue.append(node.right)
        
        nums = heapq.nsmallest(k, heap)
        return nums[-1]
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root
        while True:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            k -= 1
            if not k:
                return curr.val
            curr = curr.right
        
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(node):
            return inorder(node.left) + [node.val] + inorder(node.right) if node else []
        return inorder(root)[k - 1]
        
