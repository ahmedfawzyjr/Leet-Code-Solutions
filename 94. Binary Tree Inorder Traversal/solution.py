from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Given the root of a binary tree, return the inorder traversal of its nodes' values.
        
        Inorder traversal: Left -> Root -> Right
        
        Approach 1: Recursive (shown below)
        Approach 2: Iterative using stack
        
        Time: O(n), Space: O(h) where h is the height of the tree
        """
        result = []
        
        def inorder(node: Optional[TreeNode]) -> None:
            if not node:
                return
            inorder(node.left)
            result.append(node.val)
            inorder(node.right)
        
        inorder(root)
        return result
    
    def inorderTraversalIterative(self, root: Optional[TreeNode]) -> List[int]:
        """Iterative approach using a stack."""
        result = []
        stack = []
        curr = root
        
        while curr or stack:
            # Go to the leftmost node
            while curr:
                stack.append(curr)
                curr = curr.left
            
            # Process current node
            curr = stack.pop()
            result.append(curr.val)
            
            # Move to right subtree
            curr = curr.right
        
        return result


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
    
    # Example 1
    root1 = build_tree([1, None, 2, 3])
    print(f"Input: root = [1,null,2,3]")
    print(f"Output: {sol.inorderTraversal(root1)}")  # Expected: [1,3,2]
    
    # Example 2
    root2 = build_tree([1, 2, 3, 4, 5, None, 8, 6, 7, None, None, 9])
    print(f"\nInput: root = [1,2,3,4,5,null,8,6,7,null,null,9]")
    print(f"Output: {sol.inorderTraversal(root2)}")  # Expected: [4,2,6,5,7,1,3,9,8]
    
    # Example 3
    root3 = build_tree([])
    print(f"\nInput: root = []")
    print(f"Output: {sol.inorderTraversal(root3)}")  # Expected: []
    
    # Example 4
    root4 = build_tree([1])
    print(f"\nInput: root = [1]")
    print(f"Output: {sol.inorderTraversal(root4)}")  # Expected: [1]
