from typing import List

class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = sum(nums)
        f = sum(i * num for i, num in enumerate(nums))
        max_val = f
        
        for i in range(1, n):
            f = f + total_sum - n * nums[n-i]
            max_val = max(max_val, f)
            
        return max_val
