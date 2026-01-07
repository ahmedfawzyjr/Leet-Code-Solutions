from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        
        i = 2
        for j in range(2, len(nums)):
            if nums[j] != nums[i-2]:
                nums[i] = nums[j]
                i += 1
        
        return i

if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    nums1 = [1, 1, 1, 2, 2, 3]
    print(f"Input: nums = [1, 1, 1, 2, 2, 3]")
    k1 = sol.removeDuplicates(nums1)
    print(f"Output: {k1}, nums = {nums1[:k1]}")
    
    # Example 2
    nums2 = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    print(f"Input: nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]")
    k2 = sol.removeDuplicates(nums2)
    print(f"Output: {k2}, nums = {nums2[:k2]}")
