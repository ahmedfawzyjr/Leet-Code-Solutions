from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        Remove all occurrences of val in-place and return the count
        of remaining elements.
        
        Uses two-pointer technique: k tracks the position for
        next non-val element.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        k = 0
        
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        
        return k
