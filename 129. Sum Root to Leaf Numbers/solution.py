from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, current_sum):
            if not node:
                return 0
            
            current_sum = current_sum * 10 + node.val
            
            if not node.left and not node.right:
                return current_sum
            
            return dfs(node.left, current_sum) + dfs(node.right, current_sum)
            
        return dfs(root, 0)

if __name__ == "__main__":
    solution = Solution()
    
    # Example 1
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    output1 = solution.sumNumbers(root1)
    print(f"Example 1: Output: {output1}")
    assert output1 == 25
    
    # Example 2
    root2 = TreeNode(4)
    root2.left = TreeNode(9)
    root2.right = TreeNode(0)
    root2.left.left = TreeNode(5)
    root2.left.right = TreeNode(1)
    output2 = solution.sumNumbers(root2)
    print(f"Example 2: Output: {output2}")
    assert output2 == 1026

    print("All test cases passed!")
