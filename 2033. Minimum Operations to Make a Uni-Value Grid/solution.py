from typing import List

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        nums = []
        for row in grid:
            nums.extend(row)
        
        # All elements must have the same remainder when divided by x
        # Otherwise, we can never make them equal by adding/subtracting x
        rem = nums[0] % x
        for val in nums:
            if val % x != rem:
                return -1
        
        # The value that minimizes the sum of absolute differences |val - target|
        # is the median of the values.
        nums.sort()
        n = len(nums)
        median = nums[n // 2]
        
        total_operations = 0
        for val in nums:
            total_operations += abs(val - median) // x
            
        return total_operations
