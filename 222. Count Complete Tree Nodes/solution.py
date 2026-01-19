from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        """
        Given the root of a complete binary tree, return the number of the nodes in the tree.
        
        According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree,
        and all nodes in the last level are as far left as possible. It can have between 1 and 2^h nodes inclusive at the last level h.
        
        We can use the property of complete binary trees.
        If the height of the left subtree equals the height of the right subtree, then the left subtree is a perfect binary tree.
        Otherwise, the right subtree is a perfect binary tree (with height one less).
        
        Time Complexity: O((log N)^2)
        Space Complexity: O(log N)
        """
        if not root:
            return 0
            
        def get_height(node):
            h = 0
            while node:
                h += 1
                node = node.left
            return h
            
        left_height = get_height(root.left)
        right_height = get_height(root.right)
        
        if left_height == right_height:
            # Left subtree is a perfect binary tree of height left_height
            # Number of nodes in left subtree + root = 2^left_height - 1 + 1 = 2^left_height
            # Plus nodes in right subtree
            return (1 << left_height) + self.countNodes(root.right)
        else:
            # Right subtree is a perfect binary tree of height right_height
            # Number of nodes in right subtree + root = 2^right_height - 1 + 1 = 2^right_height
            # Plus nodes in left subtree
            return (1 << right_height) + self.countNodes(root.left)
