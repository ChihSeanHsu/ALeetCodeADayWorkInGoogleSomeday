# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def helper(node, num):
            if node is None:
                return 0
            if node.right is None and node.left is None:
                return num * 10 + node.val
            
            left = helper(node.left, num * 10 + node.val)
            right = helper(node.right, num * 10 + node.val)

            return left + right
            
        
        return helper(root, 0)
