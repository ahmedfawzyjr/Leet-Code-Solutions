from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
                
        return nums[left]

if __name__ == "__main__":
    solution = Solution()
    
    # Example 1
    nums1 = [3,4,5,1,2]
    print(f"Input: {nums1}")
    print(f"Output: {solution.findMin(nums1)}")
    # Expected: 1
    
    # Example 2
    nums2 = [4,5,6,7,0,1,2]
    print(f"Input: {nums2}")
    print(f"Output: {solution.findMin(nums2)}")
    # Expected: 0
    
    # Example 3
    nums3 = [11,13,15,17]
    print(f"Input: {nums3}")
    print(f"Output: {solution.findMin(nums3)}")
    # Expected: 11
