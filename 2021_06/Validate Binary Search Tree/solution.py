# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    last = None

    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        if not self.isValidBST(root.left):
            return False
        
        if self.last and self.last.val >= root.val:
            return False
        
        self.last = root
        
        return self.isValidBST(root.right)
