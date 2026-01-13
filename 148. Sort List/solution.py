from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        # Split the list into two halves
        left = head
        right = self.getMid(head)
        tmp = right.next
        right.next = None
        right = tmp
        
        # Recursively sort each half
        left = self.sortList(left)
        right = self.sortList(right)
        
        # Merge the sorted halves
        return self.merge(left, right)
    
    def getMid(self, head):
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def merge(self, list1, list2):
        dummy = ListNode()
        tail = dummy
        
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
            
        if list1:
            tail.next = list1
        if list2:
            tail.next = list2
            
        return dummy.next

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
    # 4 -> 2 -> 1 -> 3
    # Expected: 1 -> 2 -> 3 -> 4
    head = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))
    sorted_head = solution.sortList(head)
    print("Test Case 1: ", end="")
    print_list(sorted_head)
    
    # Test case 2
    # -1 -> 5 -> 3 -> 4 -> 0
    # Expected: -1 -> 0 -> 3 -> 4 -> 5
    head = ListNode(-1, ListNode(5, ListNode(3, ListNode(4, ListNode(0)))))
    sorted_head = solution.sortList(head)
    print("Test Case 2: ", end="")
    print_list(sorted_head)
    
    # Test case 3
    # []
    # Expected: []
    head = None
    sorted_head = solution.sortList(head)
    print("Test Case 3: ", end="")
    print_list(sorted_head)
