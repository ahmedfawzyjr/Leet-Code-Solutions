from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        Find the starting and ending position of target in a sorted array.
        Returns [-1, -1] if target is not found.
        
        Uses two binary searches: one to find the leftmost position,
        and another to find the rightmost position.
        
        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        def find_left(nums: List[int], target: int) -> int:
            """Find the leftmost (first) occurrence of target."""
            left, right = 0, len(nums) - 1
            result = -1
            
            while left <= right:
                mid = (left + right) // 2
                
                if nums[mid] == target:
                    result = mid
                    right = mid - 1  # Continue searching left
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            
            return result
        
        def find_right(nums: List[int], target: int) -> int:
            """Find the rightmost (last) occurrence of target."""
            left, right = 0, len(nums) - 1
            result = -1
            
            while left <= right:
                mid = (left + right) // 2
                
                if nums[mid] == target:
                    result = mid
                    left = mid + 1  # Continue searching right
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            
            return result
        
        return [find_left(nums, target), find_right(nums, target)]
