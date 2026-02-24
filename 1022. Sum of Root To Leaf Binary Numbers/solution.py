# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def dfs(node, current_val):
            if not node:
                return 0
            
            # Left shift the current value and add the node's value
            current_val = (current_val << 1) | node.val
            
            # If it's a leaf node, return the current path's value
            if not node.left and not node.right:
                return current_val
            
            # Sum up values from left and right subtrees
            return dfs(node.left, current_val) + dfs(node.right, current_val)
        
        return dfs(root, 0)
