from typing import List

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices:
            return 0
        
        n = len(prices)
        if k >= n // 2:
            return sum(max(prices[i+1] - prices[i], 0) for i in range(n - 1))
        
        dp = [[0] * n for _ in range(k + 1)]
        
        for i in range(1, k + 1):
            max_diff = -prices[0]
            for j in range(1, n):
                dp[i][j] = max(dp[i][j-1], prices[j] + max_diff)
                max_diff = max(max_diff, dp[i-1][j] - prices[j])
                
        return dp[k][n-1]

if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    k1 = 2
    prices1 = [2, 4, 1]
    print(f"Example 1 Output: {sol.maxProfit(k1, prices1)}")
    # Expected: 2
    
    # Example 2
    k2 = 2
    prices2 = [3, 2, 6, 5, 0, 3]
    print(f"Example 2 Output: {sol.maxProfit(k2, prices2)}")
    # Expected: 7
