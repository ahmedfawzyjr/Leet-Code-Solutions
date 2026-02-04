from typing import List
from collections import defaultdict

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n)]
        total_count = 0
        
        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                # dp[i][diff] stores number of arithmetic subsequences ending at i with diff
                # (including sequences of length 2 which are not "slices" yet)
                count = dp[j][diff]
                total_count += count
                dp[i][diff] += count + 1
                
        return total_count
