import math
from typing import List
from functools import lru_cache

class Solution:
    def getProbability(self, balls: List[int]) -> float:
        total_balls = sum(balls)
        n = total_balls // 2
        k = len(balls)
        
        # Calculate prefix sums to prune states early if remaining balls cannot satisfy the size constraint
        suffix_sums = [0] * (k + 1)
        for i in range(k - 1, -1, -1):
            suffix_sums[i] = suffix_sums[i + 1] + balls[i]

        @lru_cache(None)
        def dp(color_idx, box1_count, box1_distinct, box2_distinct):
            # Pruning: box1 cannot exceed size n, and Box 2 cannot exceed size n
            if box1_count > n:
                return 0
            # Remaining balls cannot satisfy Box 1 size n
            if box1_count + suffix_sums[color_idx] < n:
                return 0
                
            if color_idx == k:
                return 1.0 if box1_distinct == box2_distinct else 0.0
            
            ways = 0.0
            for j in range(balls[color_idx] + 1):
                ways += dp(
                    color_idx + 1,
                    box1_count + j,
                    box1_distinct + (1 if j > 0 else 0),
                    box2_distinct + (1 if balls[color_idx] - j > 0 else 0)
                ) * math.comb(balls[color_idx], j)
            return ways

        valid_ways = dp(0, 0, 0, 0)
        total_ways = math.comb(total_balls, n)
        return valid_ways / total_ways
