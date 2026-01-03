from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Search for target in a rotated sorted array.
        Returns the index of target if found, else -1.
        
        Uses modified binary search. At each step, one half is always sorted.
        We determine which half is sorted and check if target lies there.
        
        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            
            # Determine which half is sorted
            if nums[left] <= nums[mid]:
                # Left half is sorted
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                # Right half is sorted
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return -1
