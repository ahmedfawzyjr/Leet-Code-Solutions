from typing import List

class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        
        # dp_max[i][j] stores the maximum product to reach (i, j)
        # dp_min[i][j] stores the minimum product to reach (i, j)
        dp_max = [[0] * n for _ in range(m)]
        dp_min = [[0] * n for _ in range(m)]
        
        # Base case
        dp_max[0][0] = dp_min[0][0] = grid[0][0]
        
        # Initialize first row
        for j in range(1, n):
            dp_max[0][j] = dp_min[0][j] = dp_max[0][j-1] * grid[0][j]
            
        # Initialize first column
        for i in range(1, m):
            dp_max[i][0] = dp_min[i][0] = dp_max[i-1][0] * grid[i][0]
            
        # Fill the DP tables
        for i in range(1, m):
            for j in range(1, n):
                choices = [
                    dp_max[i-1][j] * grid[i][j],
                    dp_min[i-1][j] * grid[i][j],
                    dp_max[i][j-1] * grid[i][j],
                    dp_min[i][j-1] * grid[i][j]
                ]
                dp_max[i][j] = max(choices)
                dp_min[i][j] = min(choices)
        
        res = dp_max[m-1][n-1]
        return res % MOD if res >= 0 else -1

if __name__ == "__main__":
    sol = Solution()
    # Example 1
    grid1 = [[-1,-2,-3],[-2,-3,-3],[-3,-3,-2]]
    print(f"Example 1: {sol.maxProductPath(grid1)}") # Expected: -1
    
    # Example 2
    grid2 = [[1,-2,1],[1,-2,1],[3,-4,1]]
    print(f"Example 2: {sol.maxProductPath(grid2)}") # Expected: 8
    
    # Example 3
    grid3 = [[1, 3], [0, -4]]
    print(f"Example 3: {sol.maxProductPath(grid3)}") # Expected: 0
