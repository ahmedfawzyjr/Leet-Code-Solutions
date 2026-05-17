from typing import List
from collections import deque

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        # Using BFS to explore all reachable indices
        queue = deque([start])
        visited = {start}
        
        while queue:
            curr = queue.popleft()
            
            # If we reach an index with value 0, return True
            if arr[curr] == 0:
                return True
            
            # Try jumping to the right and left
            for next_idx in (curr + arr[curr], curr - arr[curr]):
                if 0 <= next_idx < len(arr) and next_idx not in visited:
                    visited.add(next_idx)
                    queue.append(next_idx)
                    
        return False

if __name__ == "__main__":
    solution = Solution()
    
    # Example 1
    arr1 = [4,2,3,0,3,1,2]
    start1 = 5
    print(f"Input: arr = {arr1}, start = {start1}")
    print(f"Output: {solution.canReach(arr1, start1)}")
    # Expected: True
    
    # Example 2
    arr2 = [4,2,3,0,3,1,2]
    start2 = 0
    print(f"Input: arr = {arr2}, start = {start2}")
    print(f"Output: {solution.canReach(arr2, start2)}")
    # Expected: True
    
    # Example 3
    arr3 = [3,0,2,1,2]
    start3 = 2
    print(f"Input: arr = {arr3}, start = {start3}")
    print(f"Output: {solution.canReach(arr3, start3)}")
    # Expected: False
