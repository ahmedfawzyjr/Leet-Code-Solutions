from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        """
        Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.
        
        We can use Dynamic Programming.
        Let dp[i][j] represent the side length of the maximum square whose bottom-right corner is the cell (i, j).
        If matrix[i][j] is '1', then dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1.
        If matrix[i][j] is '0', then dp[i][j] = 0.
        
        The base cases are the first row and first column. If matrix[i][j] is '1', dp[i][j] = 1.
        
        Time Complexity: O(m * n)
        Space Complexity: O(m * n) -> can be optimized to O(n)
        """
        if not matrix or not matrix[0]:
            return 0
            
        rows, cols = len(matrix), len(matrix[0])
        dp = [[0] * (cols + 1) for _ in range(rows + 1)]
        max_side = 0
        
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == '1':
                    dp[r+1][c+1] = min(dp[r][c+1], dp[r+1][c], dp[r][c]) + 1
                    max_side = max(max_side, dp[r+1][c+1])
                    
        return max_side * max_side
