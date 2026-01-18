from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head
        
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
            
        return prev

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
    head = to_linked_list([1,2,3,4,5])
    result = sol.reverseList(head)
    print(f"Example 1: {to_list(result)}") # Expected: [5, 4, 3, 2, 1]
    
    # Example 2
    head = to_linked_list([1,2])
    result = sol.reverseList(head)
    print(f"Example 2: {to_list(result)}") # Expected: [2, 1]
    
    # Example 3
    head = to_linked_list([])
    result = sol.reverseList(head)
    print(f"Example 3: {to_list(result)}") # Expected: []
