from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        """
        Deletes a node with the given key from a Binary Search Tree (BST).
        
        Time complexity: O(h), where h is the height of the tree.
        Space complexity: O(h) for the recursion stack.
        """
        if not root:
            return None
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # Node found
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            
            # Node with two children: Get the inorder successor (smallest in the right subtree)
            temp = self.getMin(root.right)
            root.val = temp.val
            # Delete the inorder successor
            root.right = self.deleteNode(root.right, temp.val)
            
        return root

    def getMin(self, node: TreeNode) -> TreeNode:
        while node.left:
            node = node.left
        return node
