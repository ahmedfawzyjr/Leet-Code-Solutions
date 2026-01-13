from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        
        # 1. Find the middle of the linked list
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # 2. Reverse the second half of the list
        prev = None
        curr = slow.next
        slow.next = None # Break the list into two halves
        
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            
        second_half = prev
        first_half = head
        
        # 3. Merge the two halves
        while second_half:
            temp1 = first_half.next
            temp2 = second_half.next
            
            first_half.next = second_half
            second_half.next = temp1
            
            first_half = temp1
            second_half = temp2

# Helper function to print list
def print_list(head):
    vals = []
    curr = head
    while curr:
        vals.append(curr.val)
        curr = curr.next
    print(vals)

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    # 1 -> 2 -> 3 -> 4
    # Expected: 1 -> 4 -> 2 -> 3
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    solution.reorderList(head)
    print("Test Case 1: ", end="")
    print_list(head)
    
    # Test case 2
    # 1 -> 2 -> 3 -> 4 -> 5
    # Expected: 1 -> 5 -> 2 -> 4 -> 3
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    solution.reorderList(head)
    print("Test Case 2: ", end="")
    print_list(head)
