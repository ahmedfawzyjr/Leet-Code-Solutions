from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        Find the index of target in a sorted array, or where it would be inserted.
        
        Uses binary search to find the leftmost position where target can be inserted
        while maintaining sorted order.
        
        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        left, right = 0, len(nums)
        
        while left < right:
            mid = (left + right) // 2
            
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        
        return left
