class Solution:
    def maxCollectedFruits(self, fruits: list[list[int]]) -> int:
        n = len(fruits)
        
        # 1. First child path is fixed on the diagonal: (0,0) -> (1,1) -> ... -> (n-1, n-1)
        diagonal_sum = sum(fruits[i][i] for i in range(n))
        
        # 2. Function to solve for one half (above the diagonal)
        # We need to maximize the sum of fruits collected by the second child.
        # This child starts at (0, n-1) and ends at (n-1, n-1).
        # At row r, the column c must satisfy r < c < n.
        # Transitions from row r to r+1: c can go to c-1, c, or c+1.
        # At row n-2, the only valid position that can reach (n-1, n-1) in the last step
        # is (n-2, n-1) because we must have c > r (so c > n-2 => c = n-1).
        def solve_half(grid: list[list[int]]) -> int:
            # dp[c] will store the max fruits at the current row for column c
            dp = [-float('inf')] * n
            dp[n - 1] = grid[0][n - 1]
            
            for r in range(1, n - 1):
                next_dp = [-float('inf')] * n
                # For row r, the column c must be strictly above the diagonal: r < c < n
                for c in range(r + 1, n):
                    prev_max = -float('inf')
                    # Predecessors in row r-1 could be c-1, c, c+1
                    # These predecessors must be valid for row r-1, i.e., column > r-1
                    for prev_c in (c - 1, c, c + 1):
                        if prev_c > r - 1 and prev_c < n:
                            prev_max = max(prev_max, dp[prev_c])
                    if prev_max != -float('inf'):
                        next_dp[c] = grid[r][c] + prev_max
                dp = next_dp
            
            return dp[n - 1]

        # The third child's problem (below diagonal) is symmetric to the second child
        # on the transposed grid.
        transposed_fruits = [[fruits[j][i] for j in range(n)] for i in range(n)]
        
        return diagonal_sum + solve_half(fruits) + solve_half(transposed_fruits)
