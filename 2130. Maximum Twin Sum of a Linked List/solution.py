
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # First, find the middle of the linked list
        slow, fast = head, head
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            # Reverse the first half while finding middle
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node
        
        # Now, prev is head of first half (reversed), slow is head of second half
        max_sum = 0
        while prev and slow:
            current_sum = prev.val + slow.val
            max_sum = max(max_sum, current_sum)
            prev = prev.next
            slow = slow.next
        return max_sum
