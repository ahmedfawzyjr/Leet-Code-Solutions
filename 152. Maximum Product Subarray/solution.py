from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0

        max_so_far = nums[0]
        min_so_far = nums[0]
        result = max_so_far

        for i in range(1, len(nums)):
            curr = nums[i]
            temp_max = max(curr, max(max_so_far * curr, min_so_far * curr))
            min_so_far = min(curr, min(max_so_far * curr, min_so_far * curr))
            max_so_far = temp_max
            
            result = max(max_so_far, result)

        return result

if __name__ == "__main__":
    solution = Solution()
    
    # Example 1
    nums1 = [2,3,-2,4]
    print(f"Input: {nums1}")
    print(f"Output: {solution.maxProduct(nums1)}")
    # Expected: 6
    
    # Example 2
    nums2 = [-2,0,-1]
    print(f"Input: {nums2}")
    print(f"Output: {solution.maxProduct(nums2)}")
    # Expected: 0
    
    # Extra test case
    nums3 = [-2, 3, -4]
    print(f"Input: {nums3}")
    print(f"Output: {solution.maxProduct(nums3)}")
    # Expected: 24
