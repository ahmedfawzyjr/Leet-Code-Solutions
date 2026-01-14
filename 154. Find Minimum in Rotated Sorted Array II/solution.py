from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
            else:
                right -= 1
                
        return nums[left]

if __name__ == "__main__":
    solution = Solution()
    
    # Example 1
    nums1 = [1,3,5]
    print(f"Input: {nums1}")
    print(f"Output: {solution.findMin(nums1)}")
    # Expected: 1
    
    # Example 2
    nums2 = [2,2,2,0,1]
    print(f"Input: {nums2}")
    print(f"Output: {solution.findMin(nums2)}")
    # Expected: 0
