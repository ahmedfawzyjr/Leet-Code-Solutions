from typing import List

class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        res = 0
        
        # Scenario 1: One house is at index 0
        # Search from the end for the first house with a different color
        for i in range(n - 1, 0, -1):
            if colors[i] != colors[0]:
                res = max(res, i)
                break
                
        # Scenario 2: One house is at index n-1
        # Search from the beginning for the first house with a different color
        for i in range(n - 1):
            if colors[i] != colors[n - 1]:
                res = max(res, (n - 1) - i)
                break
                
        return res
