# 104. Maximum Depth of Binary Tree
# Difficulty: Easy
# https://leetcode.com/problems/maximum-depth-of-binary-tree/

from typing import List, Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        Return the maximum depth of a binary tree.
        
        The maximum depth is the number of nodes along the longest path
        from the root node down to the farthest leaf node.
        
        Approach: Recursive DFS - depth is 1 + max(left depth, right depth)
        
        Time: O(n) where n is the number of nodes
        Space: O(h) where h is the height of the tree (recursion stack)
        """
        if not root:
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    
    def maxDepthIterative(self, root: Optional[TreeNode]) -> int:
        """
        Iterative solution using BFS (level order traversal).
        Count the number of levels.
        """
        if not root:
            return 0
        
        depth = 0
        queue = deque([root])
        
        while queue:
            depth += 1
            level_size = len(queue)
            
            for _ in range(level_size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return depth


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
    # Expected output: 3
    root1 = build_tree([3, 9, 20, None, None, 15, 7])
    result1 = sol.maxDepth(root1)
    print(f"Test 1: {result1}")
    assert result1 == 3, f"Expected 3, got {result1}"
    
    # Test case 2: root = [1,null,2]
    # Expected output: 2
    root2 = build_tree([1, None, 2])
    result2 = sol.maxDepth(root2)
    print(f"Test 2: {result2}")
    assert result2 == 2, f"Expected 2, got {result2}"
    
    # Test iterative version
    result1_iter = sol.maxDepthIterative(root1)
    result2_iter = sol.maxDepthIterative(root2)
    assert result1_iter == 3
    assert result2_iter == 2
    print("Iterative tests passed!")
    
    print("All tests passed!")
