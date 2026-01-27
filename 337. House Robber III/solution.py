from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return (0, 0) # (rob_this, skip_this)
            
            left_rob, left_skip = dfs(node.left)
            right_rob, right_skip = dfs(node.right)
            
            # If we rob this node, we must skip its children
            rob_this = node.val + left_skip + right_skip
            
            # If we skip this node, we can either rob or skip its children
            skip_this = max(left_rob, left_skip) + max(right_rob, right_skip)
            
            return (rob_this, skip_this)
            
        return max(dfs(root))

if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    # [3,2,3,null,3,null,1]
    root1 = TreeNode(3)
    root1.left = TreeNode(2, None, TreeNode(3))
    root1.right = TreeNode(3, None, TreeNode(1))
    print(f"Example 1: {sol.rob(root1)}") # Expected: 7
    
    # Example 2
    # [3,4,5,1,3,null,1]
    root2 = TreeNode(3)
    root2.left = TreeNode(4, TreeNode(1), TreeNode(3))
    root2.right = TreeNode(5, None, TreeNode(1))
    print(f"Example 2: {sol.rob(root2)}") # Expected: 9
