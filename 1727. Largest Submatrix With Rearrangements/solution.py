from typing import List

class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        heights = [0] * n
        max_area = 0
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    heights[j] += 1
                else:
                    heights[j] = 0
            
            # Sort current heights to find the best submatrix ending at this row
            # After sorting, column k will have at least sorted_heights[k] consecutive 1s
            # So a submatrix of size sorted_heights[k] x (k + 1) can be formed.
            sorted_heights = sorted(heights, reverse=True)
            for k in range(n):
                if sorted_heights[k] == 0:
                    break
                max_area = max(max_area, sorted_heights[k] * (k + 1))
        
        return max_area
