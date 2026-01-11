from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')
        
        def max_gain(node):
            if not node:
                return 0
            
            # Max sum on the left and right sub-trees of node
            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)
            
            # The price to start a new path where `node` is a highest node
            price_newpath = node.val + left_gain + right_gain
            
            # Update max_sum if it's better to start a new path
            self.max_sum = max(self.max_sum, price_newpath)
            
            # For recursion :
            # return the max gain if continue the same path
            return node.val + max(left_gain, right_gain)
        
        max_gain(root)
        return self.max_sum

if __name__ == "__main__":
    solution = Solution()
    
    # Example 1
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    output1 = solution.maxPathSum(root1)
    print(f"Example 1: Output: {output1}")
    assert output1 == 6
    
    # Example 2
    root2 = TreeNode(-10)
    root2.left = TreeNode(9)
    root2.right = TreeNode(20)
    root2.right.left = TreeNode(15)
    root2.right.right = TreeNode(7)
    output2 = solution.maxPathSum(root2)
    print(f"Example 2: Output: {output2}")
    assert output2 == 42

    print("All test cases passed!")
