from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        prev2 = 0
        prev1 = 0
        
        for num in nums:
            current = max(prev1, prev2 + num)
            prev2 = prev1
            prev1 = current
            
        return prev1

if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    nums1 = [1, 2, 3, 1]
    print(f"Input: {nums1}")
    print(f"Output: {sol.rob(nums1)}")
    # Expected: 4 (1 + 3)
    
    # Example 2
    nums2 = [2, 7, 9, 3, 1]
    print(f"Input: {nums2}")
    print(f"Output: {sol.rob(nums2)}")
    # Expected: 12 (2 + 9 + 1)
    
    # Extra case
    nums3 = [2, 1, 1, 2]
    print(f"Input: {nums3}")
    print(f"Output: {sol.rob(nums3)}")
    # Expected: 4 (2 + 2)
