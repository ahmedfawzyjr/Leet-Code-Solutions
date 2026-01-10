from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        queue = deque([(root, 1)])
        
        while queue:
            node, depth = queue.popleft()
            
            # Check if it's a leaf node
            if not node.left and not node.right:
                return depth
            
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))
        
        return 0

# Test helper to build tree from list
def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values:
        return None
    
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    
    while queue and i < len(values):
        node = queue.popleft()
        
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
    solution = Solution()
    
    # Example 1
    root1 = build_tree([3,9,20,None,None,15,7])
    result1 = solution.minDepth(root1)
    print(f"Test Case 1: Expected 2, Got {result1}")
    assert result1 == 2
    
    # Example 2
    root2 = build_tree([2,None,3,None,4,None,5,None,6])
    result2 = solution.minDepth(root2)
    print(f"Test Case 2: Expected 5, Got {result2}")
    assert result2 == 5
    
    print("All test cases passed!")
