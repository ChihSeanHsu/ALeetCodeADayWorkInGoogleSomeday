# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:

        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def inorder(node):
            if node:
                inorder(node.left)
                tmp = TreeNode(node.val)
                self.now.right = tmp
                self.now = tmp
                inorder(node.right)
                
        
        ans = self.now = TreeNode(None)
        inorder = inorder(root)
        return ans.right
        
