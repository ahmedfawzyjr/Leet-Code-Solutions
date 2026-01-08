from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        Given the root of a binary tree, determine if it is a valid binary search tree (BST).
        
        A valid BST is defined as follows:
        - The left subtree of a node contains only nodes with keys strictly less than the node's key.
        - The right subtree of a node contains only nodes with keys strictly greater than the node's key.
        - Both the left and right subtrees must also be binary search trees.
        
        Approach: Recursive validation with min/max bounds
        - For each node, track the valid range [min_val, max_val]
        - Left child must be in range [min_val, node.val)
        - Right child must be in range (node.val, max_val]
        - Time: O(n), Space: O(h) where h is the height of the tree
        """
        def validate(node: Optional[TreeNode], min_val: float, max_val: float) -> bool:
            if not node:
                return True
            
            # Check if current node's value is within valid range
            if node.val <= min_val or node.val >= max_val:
                return False
            
            # Recursively validate left and right subtrees
            return validate(node.left, min_val, node.val) and \
                   validate(node.right, node.val, max_val)
        
        return validate(root, float('-inf'), float('inf'))


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
    
    # Example 1: [2,1,3] -> true
    root1 = build_tree([2, 1, 3])
    print(f"Input: root = [2,1,3]")
    print(f"Output: {sol.isValidBST(root1)}")  # Expected: True
    
    # Example 2: [5,1,4,null,null,3,6] -> false
    root2 = build_tree([5, 1, 4, None, None, 3, 6])
    print(f"\nInput: root = [5,1,4,null,null,3,6]")
    print(f"Output: {sol.isValidBST(root2)}")  # Expected: False
