from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Remove duplicates in-place from a sorted array.
        Returns the number of unique elements k.
        
        Uses two-pointer technique: slow pointer tracks position
        for next unique element, fast pointer scans the array.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if not nums:
            return 0
        
        # Slow pointer - position for next unique element
        k = 1
        
        for i in range(1, len(nums)):
            # If current element is different from previous unique
            if nums[i] != nums[k - 1]:
                nums[k] = nums[i]
                k += 1
        
        return k
