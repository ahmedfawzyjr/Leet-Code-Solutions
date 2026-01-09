# 109. Convert Sorted List to Binary Search Tree
# Difficulty: Medium
# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/

from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        """
        Convert a sorted linked list to a height-balanced BST.
        
        Approach: Use slow/fast pointers to find the middle element,
        which becomes the root. Recursively build left and right subtrees.
        
        Time: O(n log n) - we traverse the list for each level
        Space: O(log n) for recursion stack
        """
        if not head:
            return None
        
        if not head.next:
            return TreeNode(head.val)
        
        # Find the middle element using slow/fast pointers
        # Also keep track of the node before middle to disconnect left half
        prev = None
        slow = head
        fast = head
        
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        # slow is now the middle node (root)
        # Disconnect the left half
        if prev:
            prev.next = None
        
        # Create root node
        root = TreeNode(slow.val)
        
        # Recursively build left subtree (from head to prev)
        root.left = self.sortedListToBST(head if prev else None)
        
        # Recursively build right subtree (from slow.next to end)
        root.right = self.sortedListToBST(slow.next)
        
        return root


# Helper function to create linked list from array
def create_list(arr: List[int]) -> Optional[ListNode]:
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head


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
    
    # Test case 1: head = [-10,-3,0,5,9]
    # Expected output: [0,-3,9,-10,null,5] or similar balanced BST
    head1 = create_list([-10, -3, 0, 5, 9])
    result1 = sol.sortedListToBST(head1)
    print(f"Test 1: {tree_to_list(result1)}")
    assert is_balanced(result1), "Tree should be balanced"
    
    # Test case 2: head = []
    # Expected output: []
    head2 = create_list([])
    result2 = sol.sortedListToBST(head2)
    print(f"Test 2: {tree_to_list(result2)}")
    assert result2 is None, "Expected None for empty list"
    
    # Test case 3: Single element
    head3 = create_list([0])
    result3 = sol.sortedListToBST(head3)
    print(f"Test 3: {tree_to_list(result3)}")
    assert result3.val == 0, "Expected root with value 0"
    
    print("All tests passed!")
