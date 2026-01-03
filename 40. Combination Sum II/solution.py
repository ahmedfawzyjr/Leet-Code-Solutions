from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Find all unique combinations where candidates sum to target.
        Each number may only be used once, no duplicate combinations allowed.
        
        Sort the array and skip duplicates to avoid duplicate combinations.
        
        Time Complexity: O(2^N) where N = len(candidates)
        Space Complexity: O(N) for recursion depth
        """
        result = []
        candidates.sort()  # Sort to handle duplicates easily
        
        def backtrack(start: int, current: List[int], remaining: int):
            # Base case: found a valid combination
            if remaining == 0:
                result.append(current[:])  # Add a copy
                return
            
            # Base case: exceeded target
            if remaining < 0:
                return
            
            for i in range(start, len(candidates)):
                # Skip duplicates at the same level of recursion
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                # Pruning: if current candidate exceeds remaining, stop
                if candidates[i] > remaining:
                    break
                
                current.append(candidates[i])
                # Use 'i+1' because each element can only be used once
                backtrack(i + 1, current, remaining - candidates[i])
                current.pop()  # Backtrack
        
        backtrack(0, [], target)
        return result
