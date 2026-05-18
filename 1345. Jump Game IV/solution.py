from typing import List
from collections import deque, defaultdict

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n <= 1:
            return 0
        
        # Build the graph of equal values
        val_to_indices = defaultdict(list)
        for i, val in enumerate(arr):
            val_to_indices[val].append(i)
            
        # BFS initialization
        queue = deque([(0, 0)]) # (current_index, steps)
        visited = {0}
        
        while queue:
            curr, steps = queue.popleft()
            
            # If we reach the last index, return steps
            if curr == n - 1:
                return steps
            
            # Try jumping to curr - 1 and curr + 1
            for next_idx in (curr - 1, curr + 1):
                if 0 <= next_idx < n and next_idx not in visited:
                    visited.add(next_idx)
                    queue.append((next_idx, steps + 1))
                    
            # Try jumping to all indices with the same value
            val = arr[curr]
            if val in val_to_indices:
                for next_idx in val_to_indices[val]:
                    if next_idx not in visited:
                        visited.add(next_idx)
                        queue.append((next_idx, steps + 1))
                # Optimization: clear the list of indices for this value 
                # to prevent redundant check next time we encounter the same value.
                del val_to_indices[val]
                
        return -1

if __name__ == "__main__":
    solution = Solution()
    
    # Example 1
    arr1 = [100,-23,-23,404,100,23,23,3,404]
    print(f"Input: arr = {arr1}")
    print(f"Output: {solution.minJumps(arr1)}")
    # Expected: 3
    
    # Example 2
    arr2 = [7]
    print(f"Input: arr = {arr2}")
    print(f"Output: {solution.minJumps(arr2)}")
    # Expected: 0
    
    # Example 3
    arr3 = [7,6,9,6,9,6,9,7]
    print(f"Input: arr = {arr3}")
    print(f"Output: {solution.minJumps(arr3)}")
    # Expected: 1
