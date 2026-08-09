class Solution:
    def stoneGameII(self, piles: list[int]) -> int:
        n = len(piles)
        suffix_sum = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]
            
        memo = {}
        
        def dp(i: int, m: int) -> int:
            if i + 2 * m >= n:
                return suffix_sum[i]
            if (i, m) in memo:
                return memo[(i, m)]
            
            res = 0
            for x in range(1, 2 * m + 1):
                res = max(res, suffix_sum[i] - dp(i + x, max(m, x)))
            
            memo[(i, m)] = res
            return res
            
        return dp(0, 1)
