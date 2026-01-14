from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None
        
        ptrA = headA
        ptrB = headB
        
        while ptrA != ptrB:
            ptrA = ptrA.next if ptrA else headB
            ptrB = ptrB.next if ptrB else headA
            
        return ptrA

if __name__ == "__main__":
    solution = Solution()
    
    # Example 1
    # List A: 4 -> 1 -> 8 -> 4 -> 5
    # List B: 5 -> 6 -> 1 -> 8 -> 4 -> 5
    # Intersection at 8
    
    common = ListNode(8)
    common.next = ListNode(4)
    common.next.next = ListNode(5)
    
    headA = ListNode(4)
    headA.next = ListNode(1)
    headA.next.next = common
    
    headB = ListNode(5)
    headB.next = ListNode(6)
    headB.next.next = ListNode(1)
    headB.next.next.next = common
    
    intersection = solution.getIntersectionNode(headA, headB)
    if intersection:
        print(f"Intersected at '{intersection.val}'")
    else:
        print("No intersection")
    # Expected: Intersected at '8'
    
    # Example 2
    # List A: 1 -> 9 -> 1 -> 2 -> 4
    # List B: 3 -> 2 -> 4
    # Intersection at 2
    
    common2 = ListNode(2)
    common2.next = ListNode(4)
    
    headA2 = ListNode(1)
    headA2.next = ListNode(9)
    headA2.next.next = ListNode(1)
    headA2.next.next.next = common2
    
    headB2 = ListNode(3)
    headB2.next = common2
    
    intersection2 = solution.getIntersectionNode(headA2, headB2)
    if intersection2:
        print(f"Intersected at '{intersection2.val}'")
    else:
        print("No intersection")
    # Expected: Intersected at '2'
    
    # Example 3
    # List A: 2 -> 6 -> 4
    # List B: 1 -> 5
    # No intersection
    
    headA3 = ListNode(2)
    headA3.next = ListNode(6)
    headA3.next.next = ListNode(4)
    
    headB3 = ListNode(1)
    headB3.next = ListNode(5)
    
    intersection3 = solution.getIntersectionNode(headA3, headB3)
    if intersection3:
        print(f"Intersected at '{intersection3.val}'")
    else:
        print("No intersection")
    # Expected: No intersection
