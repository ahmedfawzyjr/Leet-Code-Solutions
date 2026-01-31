from typing import List

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        # dp[stone] = set of jump lengths that reached this stone
        dp = {stone: set() for stone in stones}
        dp[0].add(0)
        
        for stone in stones:
            for k in dp[stone]:
                # Try jumps of length k-1, k, k+1
                for step in [k-1, k, k+1]:
                    if step > 0 and stone + step in dp:
                        dp[stone + step].add(step)
                        
        return len(dp[stones[-1]]) > 0
