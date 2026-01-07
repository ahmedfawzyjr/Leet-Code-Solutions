from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        before_head = ListNode(0)
        before = before_head
        after_head = ListNode(0)
        after = after_head
        
        while head:
            if head.val < x:
                before.next = head
                before = before.next
            else:
                after.next = head
                after = after.next
            head = head.next
        
        after.next = None
        before.next = after_head.next
        
        return before_head.next

def list_to_array(head: Optional[ListNode]):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res

def array_to_list(arr):
    dummy = ListNode(0)
    curr = dummy
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    head1 = array_to_list([1, 4, 3, 2, 5, 2])
    x1 = 3
    print(f"Input: head = [1, 4, 3, 2, 5, 2], x = {x1}")
    res1 = sol.partition(head1, x1)
    print(f"Output: {list_to_array(res1)}")
    
    # Example 2
    head2 = array_to_list([2, 1])
    x2 = 2
    print(f"Input: head = [2, 1], x = {x2}")
    res2 = sol.partition(head2, x2)
    print(f"Output: {list_to_array(res2)}")
