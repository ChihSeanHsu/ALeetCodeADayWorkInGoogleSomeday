# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.result = 0
        def dfs(node, curr_max):
            if node is None:
                return
            if node.val >= curr_max:
                self.result += 1
                
            curr_max = max(curr_max, node.val)
            dfs(node.left, curr_max)
            dfs(node.right, curr_max)

        # the most min number
        dfs(root, -int(1e9) + 7)
        return self.result
