# 101. Symmetric Tree
# Difficulty: Easy
# https://leetcode.com/problems/symmetric-tree/

from typing import List, Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """
        Check whether a binary tree is a mirror of itself (symmetric around its center).
        
        Approach: Recursively check if left and right subtrees are mirrors of each other.
        Two trees are mirrors if:
        1. Their root values are the same
        2. Left subtree of one is a mirror of right subtree of the other
        
        Time: O(n) where n is the number of nodes
        Space: O(h) where h is the height of the tree (recursion stack)
        """
        if not root:
            return True
        
        def is_mirror(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
            # Both empty
            if not left and not right:
                return True
            # One empty, one not
            if not left or not right:
                return False
            # Check if values match and subtrees are mirrors
            return (left.val == right.val and
                    is_mirror(left.left, right.right) and
                    is_mirror(left.right, right.left))
        
        return is_mirror(root.left, root.right)
    
    def isSymmetricIterative(self, root: Optional[TreeNode]) -> bool:
        """
        Iterative solution using a queue.
        """
        if not root:
            return True
        
        queue = deque([(root.left, root.right)])
        
        while queue:
            left, right = queue.popleft()
            
            if not left and not right:
                continue
            if not left or not right:
                return False
            if left.val != right.val:
                return False
            
            queue.append((left.left, right.right))
            queue.append((left.right, right.left))
        
        return True


# Helper function to build tree from list
def build_tree(nodes: List[Optional[int]]) -> Optional[TreeNode]:
    if not nodes or nodes[0] is None:
        return None
    
    root = TreeNode(nodes[0])
    queue = deque([root])
    i = 1
    
    while queue and i < len(nodes):
        node = queue.popleft()
        
        if i < len(nodes) and nodes[i] is not None:
            node.left = TreeNode(nodes[i])
            queue.append(node.left)
        i += 1
        
        if i < len(nodes) and nodes[i] is not None:
            node.right = TreeNode(nodes[i])
            queue.append(node.right)
        i += 1
    
    return root


# Test cases
if __name__ == "__main__":
    sol = Solution()
    
    # Test case 1: root = [1,2,2,3,4,4,3]
    # Expected output: true
    root1 = build_tree([1, 2, 2, 3, 4, 4, 3])
    result1 = sol.isSymmetric(root1)
    print(f"Test 1: {result1}")
    assert result1 == True, f"Expected True, got {result1}"
    
    # Test case 2: root = [1,2,2,null,3,null,3]
    # Expected output: false
    root2 = build_tree([1, 2, 2, None, 3, None, 3])
    result2 = sol.isSymmetric(root2)
    print(f"Test 2: {result2}")
    assert result2 == False, f"Expected False, got {result2}"
    
    # Test iterative version
    result1_iter = sol.isSymmetricIterative(root1)
    result2_iter = sol.isSymmetricIterative(root2)
    assert result1_iter == True
    assert result2_iter == False
    print("Iterative tests passed!")
    
    print("All tests passed!")
