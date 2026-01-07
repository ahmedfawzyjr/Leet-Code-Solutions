from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        """
        BFS level order traversal to find the level with maximum sum.
        
        Time: O(n) - visit each node once
        Space: O(w) - where w is the maximum width of the tree
        """
        if not root:
            return 0
        
        queue = deque([root])
        max_sum = float('-inf')
        max_level = 1
        current_level = 1
        
        while queue:
            level_size = len(queue)
            level_sum = 0
            
            for _ in range(level_size):
                node = queue.popleft()
                level_sum += node.val
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            if level_sum > max_sum:
                max_sum = level_sum
                max_level = current_level
            
            current_level += 1
        
        return max_level


# Helper function to build tree from list
def build_tree(values: list) -> Optional[TreeNode]:
    if not values:
        return None
    
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    
    while queue and i < len(values):
        node = queue.pop(0)
        
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    
    return root


# Test cases
if __name__ == "__main__":
    sol = Solution()
    
    # Test case 1
    root1 = build_tree([1, 7, 0, 7, -8, None, None])
    print(f"Test 1: {sol.maxLevelSum(root1)}")  # Expected: 2
    
    # Test case 2
    root2 = build_tree([989, None, 10250, 98693, -89388, None, None, None, -32127])
    print(f"Test 2: {sol.maxLevelSum(root2)}")  # Expected: 2
