from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Merge two sorted linked lists into one sorted linked list.
        
        Uses a dummy node and iteratively compares values from both lists,
        appending the smaller value to the result.
        
        Time Complexity: O(n + m) where n and m are the lengths of the lists
        Space Complexity: O(1)
        """
        dummy = ListNode(0)
        current = dummy
        
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        # Attach the remaining nodes
        current.next = list1 if list1 else list2
        
        return dummy.next
