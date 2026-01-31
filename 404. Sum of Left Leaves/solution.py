from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
            
        def is_leaf(node):
            return node and not node.left and not node.right
            
        res = 0
        if is_leaf(root.left):
            res += root.left.val
        
        return res + self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
