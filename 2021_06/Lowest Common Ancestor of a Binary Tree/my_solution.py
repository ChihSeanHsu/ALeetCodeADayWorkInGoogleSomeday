# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        stack = []
        find = 0
        def helper(node, find):
            store = False
            if find == 2 or node is None:
                return find
            if find == 0:
                store = True
                stack.append(node)
            if node == p or node == q:
                find += 1
            
            find = helper(node.left, find)
            find = helper(node.right, find)

            if find != 2 and store:
                stack.pop()
            return find
                
        helper(root, find)  
        return stack[-1]
            
