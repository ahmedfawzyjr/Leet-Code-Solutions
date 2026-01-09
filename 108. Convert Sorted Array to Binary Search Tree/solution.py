# 108. Convert Sorted Array to Binary Search Tree
# Difficulty: Easy
# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        """
        Convert a sorted array to a height-balanced binary search tree.
        
        Approach: Use the middle element as root, recursively build
        left subtree from left half and right subtree from right half.
        
        Time: O(n) where n is the length of the array
        Space: O(log n) for recursion stack (balanced tree)
        """
        def build(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None
            
            # Choose the middle element as root
            mid = (left + right) // 2
            root = TreeNode(nums[mid])
            
            # Recursively build left and right subtrees
            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)
            
            return root
        
        return build(0, len(nums) - 1)


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


# Helper function to check if tree is height-balanced
def is_balanced(root: Optional[TreeNode]) -> bool:
    def check(node):
        if not node:
            return 0
        left = check(node.left)
        right = check(node.right)
        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        return max(left, right) + 1
    return check(root) != -1


# Test cases
if __name__ == "__main__":
    sol = Solution()
    
    # Test case 1: nums = [-10,-3,0,5,9]
    # Expected output: [0,-3,9,-10,null,5] or [0,-10,5,null,-3,null,9]
    nums1 = [-10, -3, 0, 5, 9]
    result1 = sol.sortedArrayToBST(nums1)
    print(f"Test 1: {tree_to_list(result1)}")
    assert is_balanced(result1), "Tree should be balanced"
    
    # Test case 2: nums = [1,3]
    # Expected output: [3,1] or [1,null,3]
    nums2 = [1, 3]
    result2 = sol.sortedArrayToBST(nums2)
    print(f"Test 2: {tree_to_list(result2)}")
    assert is_balanced(result2), "Tree should be balanced"
    
    # Test case 3: Single element
    nums3 = [0]
    result3 = sol.sortedArrayToBST(nums3)
    print(f"Test 3: {tree_to_list(result3)}")
    assert result3.val == 0, "Expected root with value 0"
    
    print("All tests passed!")
