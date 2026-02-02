from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.count = 0
        self.cache = {0: 1} # prefix_sum: count
        
        def dfs(node, curr_sum):
            if not node:
                return
            
            curr_sum += node.val
            # If (curr_sum - targetSum) is in cache, it means there's a sub-path that sums to targetSum
            self.count += self.cache.get(curr_sum - targetSum, 0)
            
            # Add current prefix sum to cache
            self.cache[curr_sum] = self.cache.get(curr_sum, 0) + 1
            
            dfs(node.left, curr_sum)
            dfs(node.right, curr_sum)
            
            # Backtrack: remove current prefix sum before going up the tree
            self.cache[curr_sum] -= 1
            
        dfs(root, 0)
        return self.count
