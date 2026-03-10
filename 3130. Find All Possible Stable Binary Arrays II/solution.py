class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10**9 + 7
        
        # dp0[i][j] -> num stable arrays with i zeros, j ones ending in 0
        # dp1[i][j] -> num stable arrays with i zeros, j ones ending in 1
        dp0 = [[0] * (one + 1) for _ in range(zero + 1)]
        dp1 = [[0] * (one + 1) for _ in range(zero + 1)]
        
        # Base cases: arrays with only zeros or only ones
        for i in range(1, min(zero, limit) + 1):
            dp0[i][0] = 1
        for j in range(1, min(one, limit) + 1):
            dp1[0][j] = 1
            
        for i in range(1, zero + 1):
            for j in range(1, one + 1):
                # Ending in 0: we add a 0 to any stable array ending in 1, 
                # or add it to an array ending in 0 (unless we already have 'limit' 0s).
                # The optimized transition:
                # dp0[i][j] = sum(dp1[i-k][j] for k in range(1, limit + 1))
                dp0[i][j] = (dp0[i-1][j] + dp1[i-1][j]) % MOD
                if i > limit:
                    dp0[i][j] = (dp0[i][j] - dp1[i-limit-1][j] + MOD) % MOD
                
                # Ending in 1: symmetric logic
                dp1[i][j] = (dp0[i][j-1] + dp1[i][j-1]) % MOD
                if j > limit:
                    dp1[i][j] = (dp1[i][j] - dp0[i][j-limit-1] + MOD) % MOD
                    
        return (dp0[zero][one] + dp1[zero][one]) % MOD

if __name__ == "__main__":
    sol = Solution()
    print(f"Example 1: {sol.numberOfStableArrays(1, 1, 2)} (Expected: 2)")
    print(f"Example 2: {sol.numberOfStableArrays(1, 2, 1)} (Expected: 1)")
    print(f"Example 3: {sol.numberOfStableArrays(3, 3, 2)} (Expected: 14)")
