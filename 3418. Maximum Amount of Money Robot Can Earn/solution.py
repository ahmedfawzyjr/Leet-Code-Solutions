class Solution:
    def maximumAmount(self, coins: list[list[int]]) -> int:
        m, n = len(coins), len(coins[0])
        
        # dp[i][j][k] = maximum profit at (i, j) with k neutralizations used
        # Using at most 2 neutralizations
        
        INF = 10**15
        # dp[i][j][k]
        dp = [[[-INF] * 3 for _ in range(n)] for _ in range(m)]
        
        # Initialize start cell
        dp[0][0][0] = coins[0][0]
        # Using 1 neutralization on cell (0, 0)
        dp[0][0][1] = max(0, coins[0][0])
        # Using 2 neutralizations (but we can only use one on the same cell)
        # So dp[0][0][2] is same as dp[0][0][1]
        dp[0][0][2] = max(0, coins[0][0])
        
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                
                # Possible previous cells
                prevs = []
                if i > 0:
                    prevs.append((i - 1, j))
                if j > 0:
                    prevs.append((i, j - 1))
                
                # Case 0: No neutralizations used so far including current
                for pi, pj in prevs:
                    dp[i][j][0] = max(dp[i][j][0], dp[pi][pj][0] + coins[i][j])
                
                # Case 1: 1 neutralization used so far
                for pi, pj in prevs:
                    # Not using neutralization on current cell
                    dp[i][j][1] = max(dp[i][j][1], dp[pi][pj][1] + coins[i][j])
                    # Using neutralization on current cell
                    dp[i][j][1] = max(dp[i][j][1], dp[pi][pj][0])
                
                # Case 2: 2 neutralizations used so far
                for pi, pj in prevs:
                    # Not using neutralization on current cell
                    dp[i][j][2] = max(dp[i][j][2], dp[pi][pj][2] + coins[i][j])
                    # Using neutralization on current cell
                    dp[i][j][2] = max(dp[i][j][2], dp[pi][pj][1])
        
        return int(max(dp[m-1][n-1]))
