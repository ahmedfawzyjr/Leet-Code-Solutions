from typing import List

class Solution:
    def maximumScore(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n == 1:
            return 0
            
        pref = [[0] * (n + 1) for _ in range(n)]
        for c in range(n):
            for r in range(n):
                pref[c][r + 1] = pref[c][r] + grid[r][c]
        
        # dp[height][state]
        # state 0: decreasing (h_curr <= h_prev)
        # state 1: increasing (h_curr >= h_prev)
        dp = [[0] * 2 for _ in range(n + 1)]
        dp_prev = None
        
        for i in range(n):
            new_dp = [[0] * 2 for _ in range(n + 1)]
            
            if i == 0:
                # First column, no score yet
                pass
            else:
                # Decreasing transition: h_i <= h_{i-1}
                # new_dp[j][0] = max_{k >= j} (max(dp[k][0], dp[k][1]) + pref[i][k] - pref[i][j])
                suffix_max = -1
                for j in range(n, -1, -1):
                    suffix_max = max(suffix_max, max(dp[j][0], dp[j][1]) + pref[i][j])
                    new_dp[j][0] = suffix_max - pref[i][j]
                
                # Increasing transition: h_i >= h_{i-1}
                # new_dp[j][1] = max_{k <= j} (dp[j][1] - pref[i-1][k] + pref[i-1][j])
                prefix_max = -1
                for j in range(n + 1):
                    prefix_max = max(prefix_max, dp[j][1] - pref[i-1][j])
                    new_dp[j][1] = prefix_max + pref[i-1][j]
                
                # Valley transition: h_{i-2}=k, h_{i-1}=0, h_i=j
                if i >= 2:
                    # max_k (dp_prev[k][0] + pref[i-1][max(k, j)])
                    # prefix_max_val = max_{k <= j} dp_prev[k][0]
                    # suffix_max_val = max_{k > j} (dp_prev[k][0] + pref[i-1][k])
                    
                    # Precalculate these for all j
                    p_max = [-1] * (n + 1)
                    curr_p = -1
                    for k in range(n + 1):
                        curr_p = max(curr_p, dp_prev[k][0])
                        p_max[k] = curr_p
                        
                    s_max = [-1] * (n + 2)
                    curr_s = -1
                    for k in range(n, -1, -1):
                        curr_s = max(curr_s, dp_prev[k][0] + pref[i-1][k])
                        s_max[k] = curr_s
                        
                    for j in range(n + 1):
                        val1 = p_max[j] + pref[i-1][j]
                        val2 = s_max[j+1]
                        new_dp[j][1] = max(new_dp[j][1], val1, val2)
            
            dp_prev = dp
            dp = new_dp
            
        ans = 0
        for j in range(n + 1):
            ans = max(ans, dp[j][0], dp[j][1])
        return ans
