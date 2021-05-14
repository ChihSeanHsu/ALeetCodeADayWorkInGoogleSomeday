# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        cur = root
        while cur:
            if cur.left:
                self.flatten(cur.left)
                ori_right = cur.right
                left_end = cur.left
                while left_end.right:
                    left_end = left_end.right
                left_end.right = ori_right
                cur.right = cur.left
                cur.left = None
                cur = ori_right
            else:
                cur = cur.right

            
        
        
        
