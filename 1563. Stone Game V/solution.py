class Solution:
    def stoneGameV(self, stoneValue: list[int]) -> int:
        n = len(stoneValue)
        if n <= 1:
            return 0
        
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i+1] = pref[i] + stoneValue[i]
            
        dp = [[0] * n for _ in range(n)]
        max_left = [[0] * n for _ in range(n)]
        max_right = [[0] * n for _ in range(n)]
        
        for i in range(n):
            max_left[i][i] = stoneValue[i]
            max_right[i][i] = stoneValue[i]
            
        m = [i - 1 for i in range(n)]
        
        for L in range(2, n + 1):
            for i in range(n - L + 1):
                j = i + L - 1
                
                while m[i] + 1 < j and 2 * pref[m[i]+2] <= pref[i] + pref[j+1]:
                    m[i] += 1
                
                k = m[i]
                val = 0
                
                if k >= i:
                    sum_left = pref[k+1] - pref[i]
                    sum_right = pref[j+1] - pref[k+1]
                    if sum_left == sum_right:
                        if k - 1 >= i:
                            val = max(val, max_left[i][k-1])
                        val = max(val, sum_left + max(dp[i][k], dp[k+1][j]))
                        if k + 2 <= j:
                            val = max(val, max_right[k+2][j])
                    else:
                        val = max(val, max_left[i][k])
                        if k + 2 <= j:
                            val = max(val, max_right[k+2][j])
                else:
                    if i + 1 <= j:
                        val = max(val, max_right[i+1][j])
                        
                dp[i][j] = val
                max_left[i][j] = max(max_left[i][j-1], (pref[j+1] - pref[i]) + dp[i][j])
                max_right[i][j] = max(max_right[i+1][j], (pref[j+1] - pref[i]) + dp[i][j])
                
        return dp[0][n-1]
