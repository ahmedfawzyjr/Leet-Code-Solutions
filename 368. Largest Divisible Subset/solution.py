from typing import List

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        nums.sort()
        n = len(nums)
        dp = [1] * n
        prev = [-1] * n
        max_len = 1
        max_idx = 0
        
        for i in range(1, n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        prev[i] = j
            
            if dp[i] > max_len:
                max_len = dp[i]
                max_idx = i
                
        result = []
        curr = max_idx
        while curr != -1:
            result.append(nums[curr])
            curr = prev[curr]
            
        return result[::-1]
