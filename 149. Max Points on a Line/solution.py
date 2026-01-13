from typing import List
from collections import defaultdict
import math

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 2:
            return n
        
        max_points = 1
        
        for i in range(n):
            slopes = defaultdict(int)
            for j in range(i + 1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                
                if x1 == x2:
                    slope = float('inf')
                else:
                    slope = (y2 - y1) / (x2 - x1)
                
                slopes[slope] += 1
                max_points = max(max_points, slopes[slope] + 1)
                
        return max_points

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    # [[1,1],[2,2],[3,3]]
    # Output: 3
    points1 = [[1,1],[2,2],[3,3]]
    print(f"Test Case 1: {solution.maxPoints(points1)} (Expected: 3)")
    
    # Test case 2
    # [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
    # Output: 4
    points2 = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
    print(f"Test Case 2: {solution.maxPoints(points2)} (Expected: 4)")
