# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 is None and root2 is None:
            return
        
        val = 0
        if root1:
            val += root1.val
        if root2:
            val += root2.val
        
        new_node = TreeNode(val)
        new_node.left = self.mergeTrees(root1.left if root1 else None, root2.left if root2 else None)
        new_node.right = self.mergeTrees(root1.right if root1 else None, root2.right if root2 else None)
        
        return new_node
    
    
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 is None and root2 is None:
            return
        
        if root1 and root2:
            root1.val += root2.val
            root1.left = self.mergeTrees(root1.left, root2.left)
            root1.right = self.mergeTrees(root1.right, root2.right)
        elif root2:
            root1 = root2
        
        return root1
        
        
