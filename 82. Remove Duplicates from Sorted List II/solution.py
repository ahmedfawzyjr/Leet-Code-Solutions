from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        
        while head:
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                prev.next = head.next
            else:
                prev = prev.next
            head = head.next
            
        return dummy.next

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
    head1 = array_to_list([1, 2, 3, 3, 4, 4, 5])
    print(f"Input: head = [1, 2, 3, 3, 4, 4, 5]")
    res1 = sol.deleteDuplicates(head1)
    print(f"Output: {list_to_array(res1)}")
    
    # Example 2
    head2 = array_to_list([1, 1, 1, 2, 3])
    print(f"Input: head = [1, 1, 1, 2, 3]")
    res2 = sol.deleteDuplicates(head2)
    print(f"Output: {list_to_array(res2)}")
