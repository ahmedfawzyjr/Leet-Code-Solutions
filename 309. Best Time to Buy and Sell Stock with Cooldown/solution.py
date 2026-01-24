from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        n = len(prices)
        # buy[i]: max profit on day i ending with a buy or holding
        # sell[i]: max profit on day i ending with a sell
        # rest[i]: max profit on day i ending with a rest
        
        buy = [0] * n
        sell = [0] * n
        rest = [0] * n
        
        buy[0] = -prices[0]
        sell[0] = float('-inf')
        rest[0] = 0
        
        for i in range(1, n):
            buy[i] = max(buy[i-1], rest[i-1] - prices[i])
            sell[i] = buy[i-1] + prices[i]
            rest[i] = max(rest[i-1], sell[i-1])
            
        return max(sell[n-1], rest[n-1])
