from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        stack = [root]
        result = []
        
        while stack:
            node = stack.pop()
            result.append(node.val)
            
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
                
        return result[::-1]

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    # 1 -> null, 2 -> 3
    # Expected: [3, 2, 1]
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    print(f"Test Case 1: {solution.postorderTraversal(root)} (Expected: [3, 2, 1])")
    
    # Test case 2
    # []
    # Expected: []
    print(f"Test Case 2: {solution.postorderTraversal(None)} (Expected: [])")
    
    # Test case 3
    # 1
    # Expected: [1]
    root = TreeNode(1)
    print(f"Test Case 3: {solution.postorderTraversal(root)} (Expected: [1])")
