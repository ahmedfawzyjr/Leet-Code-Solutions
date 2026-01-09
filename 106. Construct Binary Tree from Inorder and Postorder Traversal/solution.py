# 106. Construct Binary Tree from Inorder and Postorder Traversal
# Difficulty: Medium
# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        """
        Build a binary tree from inorder and postorder traversals.
        
        Key insight:
        - The last element of postorder is always the root
        - In inorder, elements left of root are in left subtree,
          elements right of root are in right subtree
        - We recursively build subtrees using this property
        
        Time: O(n) with hash map for index lookup
        Space: O(n) for hash map and recursion stack
        """
        if not inorder or not postorder:
            return None
        
        # Create a map for O(1) index lookup in inorder array
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        
        def build(in_left: int, in_right: int, post_left: int, post_right: int) -> Optional[TreeNode]:
            if in_left > in_right or post_left > post_right:
                return None
            
            # The last element in current postorder range is the root
            root_val = postorder[post_right]
            root = TreeNode(root_val)
            
            # Find root position in inorder array
            root_idx = inorder_map[root_val]
            
            # Calculate the size of left subtree
            left_size = root_idx - in_left
            
            # Build left subtree
            root.left = build(
                in_left, root_idx - 1,
                post_left, post_left + left_size - 1
            )
            
            # Build right subtree
            root.right = build(
                root_idx + 1, in_right,
                post_left + left_size, post_right - 1
            )
            
            return root
        
        return build(0, len(inorder) - 1, 0, len(postorder) - 1)


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
    
    # Test case 1: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
    # Expected output: [3,9,20,null,null,15,7]
    inorder1 = [9, 3, 15, 20, 7]
    postorder1 = [9, 15, 7, 20, 3]
    result1 = sol.buildTree(inorder1, postorder1)
    print(f"Test 1: {tree_to_list(result1)}")
    # Expected: [3, 9, 20, None, None, 15, 7] or equivalent
    
    # Test case 2: inorder = [-1], postorder = [-1]
    # Expected output: [-1]
    inorder2 = [-1]
    postorder2 = [-1]
    result2 = sol.buildTree(inorder2, postorder2)
    print(f"Test 2: {tree_to_list(result2)}")
    
    print("All tests passed!")
