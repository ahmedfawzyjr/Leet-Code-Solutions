from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        """
        Given the head of a singly linked list and two integers left and right,
        reverse the nodes of the list from position left to position right,
        and return the reversed list.
        
        Approach: One-pass with pointer manipulation
        - Find the node before the reversal starts
        - Reverse the sublist from left to right
        - Reconnect the reversed portion
        - Time: O(n), Space: O(1)
        """
        if not head or left == right:
            return head
        
        # Create dummy node to handle edge case where left = 1
        dummy = ListNode(0)
        dummy.next = head
        
        # Move to the node before the reversal starts
        prev = dummy
        for _ in range(left - 1):
            prev = prev.next
        
        # Start reversing from this point
        curr = prev.next
        
        # Reverse nodes from left to right using the "insert at front" technique
        for _ in range(right - left):
            # Remove next_node from its current position
            next_node = curr.next
            curr.next = next_node.next
            # Insert next_node right after prev
            next_node.next = prev.next
            prev.next = next_node
        
        return dummy.next


# Helper functions
def create_linked_list(values: list) -> Optional[ListNode]:
    if not values:
        return None
    head = ListNode(values[0])
    curr = head
    for val in values[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head


def linked_list_to_list(head: Optional[ListNode]) -> list:
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    head1 = create_linked_list([1, 2, 3, 4, 5])
    left1, right1 = 2, 4
    print(f"Input: head = [1,2,3,4,5], left = {left1}, right = {right1}")
    result1 = sol.reverseBetween(head1, left1, right1)
    print(f"Output: {linked_list_to_list(result1)}")  # Expected: [1,4,3,2,5]
    
    # Example 2
    head2 = create_linked_list([5])
    left2, right2 = 1, 1
    print(f"\nInput: head = [5], left = {left2}, right = {right2}")
    result2 = sol.reverseBetween(head2, left2, right2)
    print(f"Output: {linked_list_to_list(result2)}")  # Expected: [5]
