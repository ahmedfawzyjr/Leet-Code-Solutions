from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        current = dummy
        
        while current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
                
        return dummy.next

# Helper function to convert list to linked list
def to_linked_list(elements):
    dummy = ListNode()
    current = dummy
    for el in elements:
        current.next = ListNode(val=el)
        current = current.next
    return dummy.next

# Helper function to convert linked list to list
def to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    head = to_linked_list([1,2,6,3,4,5,6])
    val = 6
    result = sol.removeElements(head, val)
    print(f"Example 1: {to_list(result)}") # Expected: [1, 2, 3, 4, 5]
    
    # Example 2
    head = to_linked_list([])
    val = 1
    result = sol.removeElements(head, val)
    print(f"Example 2: {to_list(result)}") # Expected: []
    
    # Example 3
    head = to_linked_list([7,7,7,7])
    val = 7
    result = sol.removeElements(head, val)
    print(f"Example 3: {to_list(result)}") # Expected: []
