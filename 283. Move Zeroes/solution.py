from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # lastNonZeroFoundAt keeps track of the index where the next non-zero element should be placed
        lastNonZeroFoundAt = 0
        
        # Move all non-zero elements to the front
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[lastNonZeroFoundAt], nums[i] = nums[i], nums[lastNonZeroFoundAt]
                lastNonZeroFoundAt += 1
