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
                yield from inorder(node.left)
                yield node.val
                yield from inorder(node.right)
        
        ans = now = TreeNode(None)
        for v in inorder(root):
            now.right = TreeNode(v)
            now = now.right
        return ans.right
        
