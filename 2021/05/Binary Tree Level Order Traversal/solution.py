# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        
        ans = []
        def helper(node, idx):
            if not node:
                return
            
            if len(ans) < idx + 1:
                ans.append([])
            
            ans[idx].append(node.val)    
            helper(node.left, idx + 1)
            helper(node.right, idx + 1)
            
        helper(root, 0)
        return ans
        
