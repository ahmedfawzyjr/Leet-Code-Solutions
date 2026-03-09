from typing import List

class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10**9 + 7
        
        # dp[i][j][k] is the number of stable binary arrays with i zeros and j ones,
        # ending with digit k (k=0 for '0', k=1 for '1').
        # Using a 3D DP: dp[zero + 1][one + 1][2]
        
        dp = [[[0, 0] for _ in range(one + 1)] for _ in range(zero + 1)]
        
        # Base cases: single element arrays (if they are within limit)
        for i in range(1, min(zero, limit) + 1):
            dp[i][0][0] = 1
        for j in range(1, min(one, limit) + 1):
            dp[0][j][1] = 1
            
        # Fill DP table
        for i in range(1, zero + 1):
            for j in range(1, one + 1):
                # dp[i][j][0]: ends with 0. 
                # It's the sum of dp[i-1][j][0] and dp[i-1][j][1]
                # but we must subtract cases where the last sequence of zeros exceeded 'limit'.
                # A sequence of zeros becomes >= limit+1 only if it was already 'limit' zeros long.
                # If we add a 0 to a sequence of (limit) zeros, we get (limit+1) zeros.
                # This only happens if the previous state ended with 'one' then (limit) zeros.
                # dp[i][j][0] = (dp[i-1][j][0] + dp[i-1][j][1] - (dp[i-limit-1][j][1] if i > limit else 0)) % MOD
                
                # Formula derived from prefix sums or combinatorial logic:
                # dp[i][j][0] = (dp[i-1][j][0] + dp[i-1][j][1]) 
                # If i > limit, we subtract the ways that would form a contiguous block of (limit+1) zeros.
                # That block would be: [some array with i-limit-1 zeros, j ones, ending in 1] + [limit+1 zeros]
                
                term0 = (dp[i-1][j][0] + dp[i-1][j][1]) % MOD
                if i > limit:
                    term0 = (term0 - dp[i-limit-1][j][1] + MOD) % MOD
                dp[i][j][0] = term0
                
                term1 = (dp[i][j-1][0] + dp[i][j-1][1]) % MOD
                if j > limit:
                    term1 = (term1 - dp[i][j-limit-1][0] + MOD) % MOD
                dp[i][j][1] = term1
                
        return (dp[zero][one][0] + dp[zero][one][1]) % MOD
