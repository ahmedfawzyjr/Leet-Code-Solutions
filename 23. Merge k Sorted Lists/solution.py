from typing import List, Optional
import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Merge k sorted linked lists into one sorted linked list.
        
        Uses a min-heap to efficiently get the smallest element
        among all k lists at each step.
        
        Time Complexity: O(N log k) where N is total number of nodes
        Space Complexity: O(k) for the heap
        """
        # Create a dummy head for the result list
        dummy = ListNode(0)
        current = dummy
        
        # Initialize min-heap with first node from each non-empty list
        # Heap entries: (node_value, list_index, node)
        heap = []
        for i, lst in enumerate(lists):
            if lst:
                heapq.heappush(heap, (lst.val, i, lst))
        
        while heap:
            val, i, node = heapq.heappop(heap)
            
            # Add smallest node to result
            current.next = node
            current = current.next
            
            # If there's a next node in this list, add it to heap
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
        
        return dummy.next
