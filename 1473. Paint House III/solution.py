from typing import List

class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        memo = {}
        
        def dp(i: int, target_left: int, last_color: int) -> float:
            if target_left < 0:
                return float('inf')
            if i == m:
                return 0 if target_left == 0 else float('inf')
            
            state = (i, target_left, last_color)
            if state in memo:
                return memo[state]
            
            if houses[i] != 0:
                curr_color = houses[i]
                new_target_left = target_left - (1 if curr_color != last_color else 0)
                res = dp(i + 1, new_target_left, curr_color)
            else:
                res = float('inf')
                for c in range(1, n + 1):
                    new_target_left = target_left - (1 if c != last_color else 0)
                    res = min(res, cost[i][c - 1] + dp(i + 1, new_target_left, c))
            
            memo[state] = res
            return res
        
        ans = dp(0, target, 0)
        return ans if ans != float('inf') else -1
