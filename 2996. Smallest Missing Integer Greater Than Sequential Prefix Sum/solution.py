from typing import List

class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        seq_sum = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                seq_sum += nums[i]
            else:
                break
        
        num_set = set(nums)
        curr = seq_sum
        while curr in num_set:
            curr += 1
            
        return curr
