from typing import List

class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        """
        Calculates the maximum score achievable in a grid from (0, 0) to (m-1, n-1)
        moving only right or down, such that the total cost does not exceed k.
        
        - grid[i][j] = 0: score +0, cost +0
        - grid[i][j] = 1: score +1, cost +1
        - grid[i][j] = 2: score +2, cost +1
        
        Args:
            grid: A 2D list of integers (0, 1, or 2).
            k: Maximum allowed cost.
            
        Returns:
            Maximum score or -1 if no valid path exists.
        """
        m, n = len(grid), len(grid[0])
        # dp[j][c] stores the maximum score to reach column j with cost c in the current row.
        # We use space optimization to keep only the current and previous row's DP values.
        dp = [[-1] * (k + 1) for _ in range(n)]
        
        # Base case: starting at (0, 0)
        # grid[0][0] is guaranteed to be 0, so cost is 0 and score is 0.
        dp[0][0] = 0
        
        for i in range(m):
            new_dp = [[-1] * (k + 1) for _ in range(n)]
            for j in range(n):
                v = grid[i][j]
                cost = 1 if v > 0 else 0
                
                # Special handling for (0, 0) to avoid overwriting base case
                if i == 0 and j == 0:
                    new_dp[0][0] = 0
                    continue
                
                for c in range(cost, k + 1):
                    best_prev = -1
                    # Coming from above (previous row)
                    if i > 0:
                        best_prev = max(best_prev, dp[j][c - cost])
                    # Coming from the left (current row)
                    if j > 0:
                        best_prev = max(best_prev, new_dp[j - 1][c - cost])
                    
                    if best_prev != -1:
                        new_dp[j][c] = best_prev + v
            dp = new_dp
            
        ans = max(dp[n - 1])
        return ans if ans != -1 else -1

if __name__ == "__main__":
    sol = Solution()
    # Test Case 1
    print(sol.maxPathScore([[0, 1], [2, 0]], 1))  # Expected: 2
    # Test Case 2
    print(sol.maxPathScore([[0, 1], [1, 2]], 1))  # Expected: -1
