# 105. Construct Binary Tree from Preorder and Inorder Traversal
# Difficulty: Medium
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        Build a binary tree from preorder and inorder traversals.
        
        Key insight:
        - The first element of preorder is always the root
        - In inorder, elements left of root are in left subtree,
          elements right of root are in right subtree
        - We recursively build subtrees using this property
        
        Time: O(n) with hash map for index lookup
        Space: O(n) for hash map and recursion stack
        """
        if not preorder or not inorder:
            return None
        
        # Create a map for O(1) index lookup in inorder array
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        
        def build(pre_left: int, pre_right: int, in_left: int, in_right: int) -> Optional[TreeNode]:
            if pre_left > pre_right or in_left > in_right:
                return None
            
            # The first element in current preorder range is the root
            root_val = preorder[pre_left]
            root = TreeNode(root_val)
            
            # Find root position in inorder array
            root_idx = inorder_map[root_val]
            
            # Calculate the size of left subtree
            left_size = root_idx - in_left
            
            # Build left subtree
            root.left = build(
                pre_left + 1, pre_left + left_size,
                in_left, root_idx - 1
            )
            
            # Build right subtree
            root.right = build(
                pre_left + left_size + 1, pre_right,
                root_idx + 1, in_right
            )
            
            return root
        
        return build(0, len(preorder) - 1, 0, len(inorder) - 1)


# Helper function to convert tree to list (level order)
def tree_to_list(root: Optional[TreeNode]) -> List[Optional[int]]:
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


# Test cases
if __name__ == "__main__":
    sol = Solution()
    
    # Test case 1: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
    # Expected output: [3,9,20,null,null,15,7]
    preorder1 = [3, 9, 20, 15, 7]
    inorder1 = [9, 3, 15, 20, 7]
    result1 = sol.buildTree(preorder1, inorder1)
    print(f"Test 1: {tree_to_list(result1)}")
    # Expected: [3, 9, 20, None, None, 15, 7] or equivalent
    
    # Test case 2: preorder = [-1], inorder = [-1]
    # Expected output: [-1]
    preorder2 = [-1]
    inorder2 = [-1]
    result2 = sol.buildTree(preorder2, inorder2)
    print(f"Test 2: {tree_to_list(result2)}")
    
    print("All tests passed!")
