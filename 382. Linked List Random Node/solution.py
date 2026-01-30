import random
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        # Reservoir Sampling
        # Choose the first node with probability 1
        # Choose the second node with probability 1/2
        # Choose the i-th node with probability 1/i
        
        curr = self.head
        res = curr.val
        i = 1
        
        while curr:
            if random.random() < 1/i:
                res = curr.val
            curr = curr.next
            i += 1
            
        return res

if __name__ == "__main__":
    # Test case: [1, 2, 3]
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    
    sol = Solution(head)
    
    # Statistical check (rough)
    results = {1: 0, 2: 0, 3: 0}
    for _ in range(3000):
        val = sol.getRandom()
        results[val] += 1
    
    print(results) 
    # Expected: roughly equal counts for 1, 2, 3 (around 1000 each)
