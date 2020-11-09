# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        # (node, max, min)
        stack = [(root, root.val, root.val)]
        result = 0
        while stack:
            node, parent_max, parent_min = stack.pop()
            parent_max = max(parent_max, node.val)
            parent_min = min(parent_min, node.val)
            result = max(result, abs(parent_max - parent_min))
            
            if node.left:
                stack.append((node.left, parent_max, parent_min))
            if node.right:
                stack.append((node.right, parent_max, parent_min))
        
        return result
        
        
                
