# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        if root is None:
            return []
        
        if root.val == targetSum and root.right is None and root.left is None:
            return [[root.val]]
        
        left_side_paths = self.pathSum(root.left, targetSum - root.val)
        right_side_paths = self.pathSum(root.right, targetSum - root.val)
        
        return [[root.val] + path for path in left_side_paths] + [[root.val] + path for path in right_side_paths]
