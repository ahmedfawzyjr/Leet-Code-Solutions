from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Find all unique combinations where candidates sum to target.
        The same number may be chosen an unlimited number of times.
        
        Uses backtracking with a starting index to avoid duplicates.
        
        Time Complexity: O(N^(T/M)) where N = len(candidates), T = target, M = min(candidates)
        Space Complexity: O(T/M) for recursion depth
        """
        result = []
        
        def backtrack(start: int, current: List[int], remaining: int):
            # Base case: found a valid combination
            if remaining == 0:
                result.append(current[:])  # Add a copy
                return
            
            # Base case: exceeded target
            if remaining < 0:
                return
            
            # Try each candidate starting from 'start' to avoid duplicates
            for i in range(start, len(candidates)):
                current.append(candidates[i])
                # Use 'i' (not i+1) because same element can be reused
                backtrack(i, current, remaining - candidates[i])
                current.pop()  # Backtrack
        
        backtrack(0, [], target)
        return result
