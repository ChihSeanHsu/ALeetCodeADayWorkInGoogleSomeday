from collections import defaultdict

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        node_depth = defaultdict(list)
        stack = [(root, 1, None)]
        result = False
        while stack:
            node, depth, parent = stack.pop()
            node_depth[node.val] = (depth, parent)
            if node.left:
                stack.append((node.left, depth + 1, node))
            if node.right:
                stack.append((node.right, depth + 1, node))
                
        if node_depth[x][0] == node_depth[y][0] and node_depth[x][1] != node_depth[y][1]:
            result = True
            
        return result
        
