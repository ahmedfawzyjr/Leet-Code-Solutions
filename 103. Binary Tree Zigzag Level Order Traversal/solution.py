# 103. Binary Tree Zigzag Level Order Traversal
# Difficulty: Medium
# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

from typing import List, Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Return the zigzag level order traversal of a binary tree.
        (i.e., from left to right, then right to left for the next level and alternate between)
        
        Approach: BFS with a flag to track direction, reverse alternate levels.
        
        Time: O(n) where n is the number of nodes
        Space: O(n) for the queue and result
        """
        if not root:
            return []
        
        result = []
        queue = deque([root])
        left_to_right = True
        
        while queue:
            level_size = len(queue)
            level = deque()
            
            for _ in range(level_size):
                node = queue.popleft()
                
                # Add to level based on direction
                if left_to_right:
                    level.append(node.val)
                else:
                    level.appendleft(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(list(level))
            left_to_right = not left_to_right
        
        return result


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
    # Expected output: [[3],[20,9],[15,7]]
    root1 = build_tree([3, 9, 20, None, None, 15, 7])
    result1 = sol.zigzagLevelOrder(root1)
    print(f"Test 1: {result1}")
    assert result1 == [[3], [20, 9], [15, 7]], f"Expected [[3], [20, 9], [15, 7]], got {result1}"
    
    # Test case 2: root = [1]
    # Expected output: [[1]]
    root2 = build_tree([1])
    result2 = sol.zigzagLevelOrder(root2)
    print(f"Test 2: {result2}")
    assert result2 == [[1]], f"Expected [[1]], got {result2}"
    
    # Test case 3: root = []
    # Expected output: []
    root3 = build_tree([])
    result3 = sol.zigzagLevelOrder(root3)
    print(f"Test 3: {result3}")
    assert result3 == [], f"Expected [], got {result3}"
    
    print("All tests passed!")
