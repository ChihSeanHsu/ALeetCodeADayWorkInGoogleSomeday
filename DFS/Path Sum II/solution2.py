# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        result = []
        stack = [[root, targetSum, []]]
        while stack:
            node, ts, node_list = stack.pop()
            if node is None:
                continue
            
            if node.val == ts and node.right is None and node.left is None:
                result.append(node_list + [node.val])
            
            stack.append([node.right, ts - node.val, node_list + [node.val]])
            stack.append([node.left, ts - node.val, node_list + [node.val]])
                
        return result
