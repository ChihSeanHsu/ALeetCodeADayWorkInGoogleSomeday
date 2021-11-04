# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        result = 0
        if root.left and root.left.right is None and root.left.left is None:
            result += root.left.val
            
        result += self.sumOfLeftLeaves(root.left)
        result += self.sumOfLeftLeaves(root.right)
        return result
