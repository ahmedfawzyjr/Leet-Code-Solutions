from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        
        slow = head
        fast = head.next
        
        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
            
        return True

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: Cycle exists
    # 3 -> 2 -> 0 -> -4 -> 2
    node1 = ListNode(3)
    node2 = ListNode(2)
    node3 = ListNode(0)
    node4 = ListNode(-4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2 # Cycle
    
    print(f"Test Case 1: {solution.hasCycle(node1)} (Expected: True)")
    
    # Test case 2: Cycle exists
    # 1 -> 2 -> 1
    node1 = ListNode(1)
    node2 = ListNode(2)
    node1.next = node2
    node2.next = node1 # Cycle
    
    print(f"Test Case 2: {solution.hasCycle(node1)} (Expected: True)")
    
    # Test case 3: No cycle
    # 1
    node1 = ListNode(1)
    print(f"Test Case 3: {solution.hasCycle(node1)} (Expected: False)")
