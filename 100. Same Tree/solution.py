from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        Given the roots of two binary trees p and q, write a function to check if 
        they are the same or not.
        
        Two binary trees are considered the same if they are structurally identical, 
        and the nodes have the same value.
        
        Approach: Recursive comparison
        - Base cases: both null (same), one null (different)
        - If values differ, not the same
        - Recursively check left and right subtrees
        - Time: O(n), Space: O(h) where h is the height
        """
        # Both are None - same
        if not p and not q:
            return True
        
        # One is None, other is not - different
        if not p or not q:
            return False
        
        # Values differ - different
        if p.val != q.val:
            return False
        
        # Recursively check both subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


# Helper function to build tree from list
def build_tree(values: list) -> Optional[TreeNode]:
    if not values or values[0] is None:
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


if __name__ == "__main__":
    sol = Solution()
    
    # Example 1: p = [1,2,3], q = [1,2,3] -> true
    p1 = build_tree([1, 2, 3])
    q1 = build_tree([1, 2, 3])
    print(f"Input: p = [1,2,3], q = [1,2,3]")
    print(f"Output: {sol.isSameTree(p1, q1)}")  # Expected: True
    
    # Example 2: p = [1,2], q = [1,null,2] -> false
    p2 = build_tree([1, 2])
    q2 = build_tree([1, None, 2])
    print(f"\nInput: p = [1,2], q = [1,null,2]")
    print(f"Output: {sol.isSameTree(p2, q2)}")  # Expected: False
    
    # Example 3: p = [1,2,1], q = [1,1,2] -> false
    p3 = build_tree([1, 2, 1])
    q3 = build_tree([1, 1, 2])
    print(f"\nInput: p = [1,2,1], q = [1,1,2]")
    print(f"Output: {sol.isSameTree(p3, q3)}")  # Expected: False
