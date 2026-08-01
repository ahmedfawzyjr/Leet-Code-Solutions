from typing import List
from collections import defaultdict

class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        # Map each value to the set of row indices containing it
        value_to_rows = defaultdict(list)
        for r, row in enumerate(grid):
            # Using set to avoid duplicate rows for the same value
            for val in set(row):
                value_to_rows[val].append(r)
        
        # Sort unique values in descending order
        values = sorted(value_to_rows.keys(), reverse=True)
        
        # Memoization dictionary
        memo = {}
        
        def dp(index: int, mask: int) -> int:
            if index == len(values):
                return 0
            
            state = (index, mask)
            if state in memo:
                return memo[state]
            
            val = values[index]
            # Option 1: Do not select the current value
            ans = dp(index + 1, mask)
            
            # Option 2: Select the current value from one of the rows it appears in
            for r in value_to_rows[val]:
                if not (mask & (1 << r)):
                    ans = max(ans, val + dp(index + 1, mask | (1 << r)))
            
            memo[state] = ans
            return ans
            
        return dp(0, 0)
