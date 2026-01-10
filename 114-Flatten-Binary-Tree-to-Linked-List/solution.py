from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        
        # Flatten left and right subtrees
        self.flatten(root.left)
        self.flatten(root.right)
        
        # Store right subtree
        right_subtree = root.right
        
        # Move left subtree to right
        root.right = root.left
        root.left = None
        
        # Find the end of the new right subtree (which was the left subtree)
        current = root
        while current.right:
            current = current.right
            
        # Attach the original right subtree
        current.right = right_subtree

def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root

def tree_to_list(root: Optional[TreeNode]) -> List[Optional[int]]:
    result = []
    current = root
    while current:
        result.append(current.val)
        result.append(None) # For the null left child
        current = current.right
    # Remove the last None if it exists (though the problem output format is a bit specific, 
    # we'll just check the structure)
    return result

def check_flattened(root: Optional[TreeNode], expected_values: List[int]) -> bool:
    current = root
    for val in expected_values:
        if not current:
            return False
        if current.val != val:
            return False
        if current.left is not None:
            return False
        current = current.right
    return current is None

if __name__ == "__main__":
    solution = Solution()
    
    # Example 1
    root1 = build_tree([1,2,5,3,4,None,6])
    solution.flatten(root1)
    # Expected: 1 -> 2 -> 3 -> 4 -> 5 -> 6
    expected1 = [1, 2, 3, 4, 5, 6]
    assert check_flattened(root1, expected1), "Test case 1 failed"
    print("Test case 1 passed")
    
    # Example 2
    root2 = build_tree([])
    solution.flatten(root2)
    assert root2 is None, "Test case 2 failed"
    print("Test case 2 passed")
    
    # Example 3
    root3 = build_tree([0])
    solution.flatten(root3)
    assert check_flattened(root3, [0]), "Test case 3 failed"
    print("Test case 3 passed")
    
    print("All test cases passed!")
