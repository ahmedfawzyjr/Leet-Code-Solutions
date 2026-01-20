from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        
        # Find middle
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # Reverse second half
        prev = None
        curr = slow
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
            
        # Compare halves
        left, right = head, prev
        while right: # Only need to check right half length
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
            
        return True

if __name__ == "__main__":
    sol = Solution()
    
    # [1,2,2,1]
    head1 = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
    print(f"Is [1,2,2,1] palindrome? {sol.isPalindrome(head1)}") # True
    
    # [1,2]
    head2 = ListNode(1, ListNode(2))
    print(f"Is [1,2] palindrome? {sol.isPalindrome(head2)}") # False
