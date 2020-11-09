# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        max_num, min_num = root.val, root.val
        left, right = 0, 0
        if root.left:
            left = self.get_diff(root.left, max_num, min_num)
        if root.right:
            right = self.get_diff(root.right, max_num, min_num)
        return max(left, right)
        
    def get_diff(self, root: TreeNode, max_num: int, min_num: int) -> int:
        max_num = max(max_num, root.val)
        min_num = min(min_num, root.val)

        if root.left or root.right:
            left, right = 0, 0
            if root.left:
                left = self.get_diff(root.left, max_num, min_num)
            if root.right:
                right = self.get_diff(root.right, max_num, min_num)
            return max(left, right)
        else:
            return abs(max_num - min_num)
        
        
                
    
        
    
        
        
