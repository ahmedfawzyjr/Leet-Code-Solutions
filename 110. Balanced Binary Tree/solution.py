# 110. Balanced Binary Tree
# Difficulty: Easy
# https://leetcode.com/problems/balanced-binary-tree/

from typing import List, Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        Check if a binary tree is height-balanced.
        
        A height-balanced binary tree is defined as a binary tree in which
        the depth of the two subtrees of every node never differ by more than 1.
        
        Approach: Bottom-up recursion - compute height and check balance
        in a single pass.
        
        Time: O(n) where n is the number of nodes
        Space: O(h) where h is the height of the tree (recursion stack)
        """
        def check_height(node: Optional[TreeNode]) -> int:
            """
            Returns the height of the subtree if balanced, -1 if unbalanced.
            """
            if not node:
                return 0
            
            # Check left subtree
            left_height = check_height(node.left)
            if left_height == -1:
                return -1
            
            # Check right subtree
            right_height = check_height(node.right)
            if right_height == -1:
                return -1
            
            # Check if current node is balanced
            if abs(left_height - right_height) > 1:
                return -1
            
            return max(left_height, right_height) + 1
        
        return check_height(root) != -1


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
    
    # Test case 1: root = [3,9,20,null,null,15,7]
    # Expected output: true
    root1 = build_tree([3, 9, 20, None, None, 15, 7])
    result1 = sol.isBalanced(root1)
    print(f"Test 1: {result1}")
    assert result1 == True, f"Expected True, got {result1}"
    
    # Test case 2: root = [1,2,2,3,3,null,null,4,4]
    # Expected output: false
    root2 = build_tree([1, 2, 2, 3, 3, None, None, 4, 4])
    result2 = sol.isBalanced(root2)
    print(f"Test 2: {result2}")
    assert result2 == False, f"Expected False, got {result2}"
    
    # Test case 3: root = []
    # Expected output: true
    root3 = build_tree([])
    result3 = sol.isBalanced(root3)
    print(f"Test 3: {result3}")
    assert result3 == True, f"Expected True, got {result3}"
    
    print("All tests passed!")
