from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            if nums[mid] > nums[mid + 1]:
                # We are in a descending sequence, so peak must be at mid or to the left
                right = mid
            else:
                # We are in an ascending sequence, so peak must be to the right
                left = mid + 1
                
        return left

if __name__ == "__main__":
    solution = Solution()
    
    # Example 1
    nums1 = [1,2,3,1]
    print(f"Input: {nums1}")
    print(f"Output: {solution.findPeakElement(nums1)}")
    # Expected: 2
    
    # Example 2
    nums2 = [1,2,1,3,5,6,4]
    print(f"Input: {nums2}")
    print(f"Output: {solution.findPeakElement(nums2)}")
    # Expected: 5 (or 1)
