# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        result = float("-inf")
        sub_sums = set()
        
        def dfs(node):
            if node is None:
                return 0
            right = dfs(node.right)
            left = dfs(node.left)
            sub_sum = right + left + node.val
            sub_sums.add(sub_sum)
            return sub_sum
        
        tree_sum = dfs(root)
        for i in sub_sums:
            result = max(result, (tree_sum - i) * i)
        
        return result % 1000000007
        
        
        
