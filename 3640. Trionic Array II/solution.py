from typing import List

class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 4:
            return 0
            
        # inc[i]: max sum of strictly increasing subarray ending at i
        inc = [0] * n
        # mountain[i]: max sum of nums[j...i] such that j < p < i
        # where nums[j...p] is strictly increasing and nums[p...i] is strictly decreasing
        mountain = [float('-inf')] * n
        # trionic[i]: max sum of nums[j...i] such that j < p < q < i
        # where nums[j...p] inc, nums[p...q] dec, nums[q...i] inc
        trionic = [float('-inf')] * n
        
        inc[0] = nums[0]
        
        for i in range(1, n):
            # Strictly increasing
            if nums[i] > nums[i-1]:
                inc[i] = inc[i-1] + nums[i]
            else:
                inc[i] = nums[i]
                
            # Strictly decreasing (mountain)
            if nums[i] < nums[i-1]:
                # Start from peak at i-1: we need nums[i-1] > nums[i-2]
                if i >= 2 and nums[i-1] > nums[i-2]:
                    mountain[i] = max(mountain[i], inc[i-1] + nums[i])
                # Extend existing mountain
                if mountain[i-1] != float('-inf'):
                    mountain[i] = max(mountain[i], mountain[i-1] + nums[i])
            
            # Strictly increasing (trionic)
            if nums[i] > nums[i-1]:
                # Start third part from mountain ending at i-1
                if mountain[i-1] != float('-inf'):
                    trionic[i] = max(trionic[i], mountain[i-1] + nums[i])
                # Extend existing trionic
                if trionic[i-1] != float('-inf'):
                    trionic[i] = max(trionic[i], trionic[i-1] + nums[i])
                    
        ans = max(trionic)
        return int(ans) if ans != float('-inf') else 0
