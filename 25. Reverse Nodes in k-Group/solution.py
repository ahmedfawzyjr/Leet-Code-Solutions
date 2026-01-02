from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        Reverse nodes in k-sized groups.
        
        If the number of remaining nodes is less than k, they remain as-is.
        Only nodes themselves may be changed, not their values.
        
        Time Complexity: O(n) where n is the number of nodes
        Space Complexity: O(1)
        """
        # Count total nodes
        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next
        
        dummy = ListNode(0, head)
        group_prev = dummy
        
        while count >= k:
            # Reverse k nodes starting from group_prev.next
            curr = group_prev.next
            next_node = curr.next
            
            # Perform k-1 swaps to reverse k nodes
            for _ in range(k - 1):
                curr.next = next_node.next
                next_node.next = group_prev.next
                group_prev.next = next_node
                next_node = curr.next
            
            # Move group_prev to the end of the reversed group
            group_prev = curr
            count -= k
        
        return dummy.next
