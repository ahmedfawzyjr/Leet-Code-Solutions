from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        """
        Given an integer n, return all the structurally unique BST's (binary search trees),
        which has exactly n nodes of unique values from 1 to n.
        
        Approach: Recursive generation
        - For each value i from 1 to n as root:
          - Left subtree contains values [1, i-1]
          - Right subtree contains values [i+1, n]
        - Recursively generate all possible left and right subtrees
        - Combine each left subtree with each right subtree
        - Time: O(4^n / sqrt(n)) - Catalan number
        """
        if n == 0:
            return []
        
        def generate(start: int, end: int) -> List[Optional[TreeNode]]:
            if start > end:
                return [None]
            
            all_trees = []
            
            for root_val in range(start, end + 1):
                # Generate all possible left subtrees
                left_trees = generate(start, root_val - 1)
                # Generate all possible right subtrees
                right_trees = generate(root_val + 1, end)
                
                # Combine each left with each right
                for left in left_trees:
                    for right in right_trees:
                        root = TreeNode(root_val)
                        root.left = left
                        root.right = right
                        all_trees.append(root)
            
            return all_trees
        
        return generate(1, n)


def tree_to_list(root: Optional[TreeNode]) -> list:
    """Convert tree to list representation for output."""
    if not root:
        return []
    
    result = []
    queue = [root]
    
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    
    # Remove trailing Nones
    while result and result[-1] is None:
        result.pop()
    
    return result


if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    n1 = 3
    print(f"Input: n = {n1}")
    trees1 = sol.generateTrees(n1)
    print(f"Output: {[tree_to_list(t) for t in trees1]}")
    # Expected: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]
    
    # Example 2
    n2 = 1
    print(f"\nInput: n = {n2}")
    trees2 = sol.generateTrees(n2)
    print(f"Output: {[tree_to_list(t) for t in trees2]}")
    # Expected: [[1]]
