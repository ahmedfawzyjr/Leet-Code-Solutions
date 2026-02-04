from typing import List

class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 4:
            return 0
            
        # inc1[i]: max sum of strictly increasing subarray ending at i (length >= 1)
        inc1 = [0.0] * n
        # inc2[i]: max sum of strictly increasing subarray ending at i (length >= 2)
        inc2 = [float('-inf')] * n
        # mountain[i]: max sum of nums[j...i] such that j < p < i (length >= 3)
        mountain = [float('-inf')] * n
        # trionic[i]: max sum of nums[j...i] such that j < p < q < i (length >= 4)
        trionic = [float('-inf')] * n
        
        inc1[0] = float(nums[0])
        
        for i in range(1, n):
            # Strictly increasing
            if nums[i] > nums[i-1]:
                inc1[i] = max(float(nums[i]), inc1[i-1] + nums[i])
                inc2[i] = inc1[i-1] + nums[i]
            else:
                inc1[i] = float(nums[i])
                
            # Strictly decreasing (mountain)
            if nums[i] < nums[i-1]:
                # Start dec from some inc2 at i-1
                if inc2[i-1] != float('-inf'):
                    mountain[i] = max(mountain[i], inc2[i-1] + nums[i])
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
