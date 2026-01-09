# LeetCode 95. Unique Binary Search Trees II
# 
# IMPORTANT: When submitting to LeetCode, ONLY copy the Solution class below.
# Do NOT copy the TreeNode class - LeetCode provides it.

from typing import List, Optional

# Definition for a binary tree node (for local testing only).
# LeetCode already provides this - DO NOT include when submitting!
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ============= COPY FROM HERE FOR LEETCODE SUBMISSION =============

class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        """
        Given an integer n, return all the structurally unique BST's
        which has exactly n nodes of unique values from 1 to n.
        """
        
        def build(lo: int, hi: int) -> List[Optional[TreeNode]]:
            if lo > hi:
                return [None]
            
            result = []
            for val in range(lo, hi + 1):
                # Generate all left subtrees with values [lo, val-1]
                for left in build(lo, val - 1):
                    # Generate all right subtrees with values [val+1, hi]
                    for right in build(val + 1, hi):
                        node = TreeNode(val)
                        node.left = left
                        node.right = right
                        result.append(node)
            
            return result
        
        return build(1, n)

# ============= END OF LEETCODE SUBMISSION =============


# Local testing code (do not submit to LeetCode)
def tree_to_list(root):
    if not root:
        return []
    result, queue = [], [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    return result


if __name__ == "__main__":
    sol = Solution()
    
    print("Input: n = 3")
    trees = sol.generateTrees(3)
    print(f"Output: {[tree_to_list(t) for t in trees]}")
    print(f"Count: {len(trees)} trees")  # Should be 5
    
    print("\nInput: n = 1")
    trees = sol.generateTrees(1)
    print(f"Output: {[tree_to_list(t) for t in trees]}")
