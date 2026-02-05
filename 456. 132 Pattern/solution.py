from typing import List

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        """
        Finds if there is a 132 pattern in the sequence.
        Pattern is nums[i] < nums[k] < nums[j] with i < j < k.
        
        Time complexity: O(n)
        Space complexity: O(n) for the stack.
        """
        if len(nums) < 3:
            return False
        
        # s3 is the potential nums[k] (the '2' in 132)
        s3 = float('-inf')
        stack = []
        
        # Iterate from right to left
        for i in range(len(nums) - 1, -1, -1):
            # If we find a number smaller than s3, we have 132 pattern (nums[i] < s3)
            # because s3 was already verified to be smaller than some nums[j] to its left
            if nums[i] < s3:
                return True
            
            # If nums[i] is greater than the top of the stack, update s3
            # and pop until the stack top is greater than nums[i]
            while stack and nums[i] > stack[-1]:
                s3 = stack.pop()
            
            # Push current number as potential nums[j] (the '3' in 132)
            stack.append(nums[i])
            
        return False
