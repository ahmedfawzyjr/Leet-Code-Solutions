from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head

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
    head1 = array_to_list([1, 1, 2])
    print(f"Input: head = [1, 1, 2]")
    res1 = sol.deleteDuplicates(head1)
    print(f"Output: {list_to_array(res1)}")
    
    # Example 2
    head2 = array_to_list([1, 1, 2, 3, 3])
    print(f"Input: head = [1, 1, 2, 3, 3]")
    res2 = sol.deleteDuplicates(head2)
    print(f"Output: {list_to_array(res2)}")
