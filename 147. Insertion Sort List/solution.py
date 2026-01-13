from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        dummy = ListNode(0)
        curr = head
        
        while curr:
            prev = dummy
            # Find the position to insert
            while prev.next and prev.next.val < curr.val:
                prev = prev.next
            
            next_node = curr.next
            
            # Insert curr between prev and prev.next
            curr.next = prev.next
            prev.next = curr
            
            curr = next_node
            
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
    sorted_head = solution.insertionSortList(head)
    print("Test Case 1: ", end="")
    print_list(sorted_head)
    
    # Test case 2
    # -1 -> 5 -> 3 -> 4 -> 0
    # Expected: -1 -> 0 -> 3 -> 4 -> 5
    head = ListNode(-1, ListNode(5, ListNode(3, ListNode(4, ListNode(0)))))
    sorted_head = solution.insertionSortList(head)
    print("Test Case 2: ", end="")
    print_list(sorted_head)
