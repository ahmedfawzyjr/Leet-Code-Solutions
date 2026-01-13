from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        
        slow = head
        fast = head
        
        # Detect cycle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return None # No cycle found
        
        # Find entry point
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
            
        return slow

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
    node4.next = node2 # Cycle at index 1 (node2)
    
    result = solution.detectCycle(node1)
    print(f"Test Case 1: {result.val if result else None} (Expected: 2)")
    
    # Test case 2: Cycle exists
    # 1 -> 2 -> 1
    node1 = ListNode(1)
    node2 = ListNode(2)
    node1.next = node2
    node2.next = node1 # Cycle at index 0 (node1)
    
    result = solution.detectCycle(node1)
    print(f"Test Case 2: {result.val if result else None} (Expected: 1)")
    
    # Test case 3: No cycle
    # 1
    node1 = ListNode(1)
    result = solution.detectCycle(node1)
    print(f"Test Case 3: {result.val if result else None} (Expected: None)")
