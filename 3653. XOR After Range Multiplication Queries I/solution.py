from typing import List

class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        MOD = 10**9 + 7
        for l, r, k, v in queries:
            if v == 1:
                continue
            for i in range(l, r + 1, k):
                nums[i] = (nums[i] * v) % MOD
        
        res = 0
        for x in nums:
            res ^= x
        return res
