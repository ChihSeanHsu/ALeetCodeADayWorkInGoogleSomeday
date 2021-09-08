# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        def helper(node, depth):
            if node is None:
                return True, depth
            
            left_b, left_h = helper(node.left, depth + 1)
            if left_b is False:
                return False, left_h
            
            right_b, right_h = helper(node.right, depth + 1)
            if right_b is False:
                return False, right_h
            
            return abs(left_h - right_h) <= 1, max(left_h, right_h)
        
        return helper(root, 0)[0]
        
