class Solution:
    def getMoneyAmount(self, n: int) -> int:
        # dp[i][j] represents the minimum amount of money you need to guarantee a win
        # for the range [i, j].
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        
        for length in range(2, n + 1):
            for start in range(1, n - length + 2):
                end = start + length - 1
                min_cost = float('inf')
                
                # Try every pivot k in [start, end]
                # If we guess k, the cost is k + max(cost(start, k-1), cost(k+1, end))
                # We want to minimize this cost over all possible k.
                # Optimization: k only needs to go from start + (length-1)//2 to end - 1
                # because the answer will likely be near the middle or slightly to the right.
                # But for correctness and simplicity given constraints (n <= 200), full range is fine.
                
                for k in range(start, end):
                    cost = k + max(dp[start][k-1], dp[k+1][end])
                    min_cost = min(min_cost, cost)
                
                # If we pick 'end', the cost is end + dp[start][end-1] (since right side is empty)
                # Actually the loop above covers k up to end-1.
                # If k = end, cost = end + dp[start][end-1]
                cost_end = end + dp[start][end-1]
                min_cost = min(min_cost, cost_end)
                
                dp[start][end] = min_cost
                
        return dp[1][n]
