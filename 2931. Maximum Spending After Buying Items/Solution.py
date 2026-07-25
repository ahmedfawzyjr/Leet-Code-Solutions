from typing import List

class Solution:
    def maxSpending(self, values: List[List[int]]) -> int:
        all_values = []
        for row in values:
            all_values.extend(row)
        
        all_values.sort()
        
        total_spending = 0
        for day, val in enumerate(all_values, 1):
            total_spending += day * val
            
        return total_spending
