# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return
        
        def search_node(node, prev):
            if node is None:
                return node              
            if node.val == key:
                if not node.right is None:
                    new_node = node.right
                    curr = new_node
                    while curr and curr.left:
                        curr = curr.left
                    if node.left:
                        curr.left = node.left
                else:
                    new_node = node.left
                return new_node
            
            if key > node.val:
                node.right = search_node(node.right, node)
            elif key < node.val:
                node.left = search_node(node.left, node)
            
            return node
                    
            
        return search_node(root, None)
