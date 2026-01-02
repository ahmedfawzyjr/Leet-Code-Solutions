from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Swap every two adjacent nodes in a linked list.
        
        Uses a dummy node and iterative approach to swap pairs
        by manipulating the next pointers.
        
        Time Complexity: O(n) where n is the number of nodes
        Space Complexity: O(1)
        """
        dummy = ListNode(0, head)
        prev = dummy
        
        while prev.next and prev.next.next:
            # Nodes to be swapped
            first = prev.next
            second = prev.next.next
            
            # Perform the swap
            prev.next = second
            first.next = second.next
            second.next = first
            
            # Move prev pointer forward for next pair
            prev = first
        
        return dummy.next
