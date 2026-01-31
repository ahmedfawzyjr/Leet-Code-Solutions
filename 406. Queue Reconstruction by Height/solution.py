from typing import List

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # Sort by height descending, then by k ascending
        people.sort(key=lambda x: (-x[0], x[1]))
        
        queue = []
        for p in people:
            # Insert at the k-th position
            queue.insert(p[1], p)
            
        return queue
