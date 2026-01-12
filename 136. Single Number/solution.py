from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result

if __name__ == "__main__":
    solution = Solution()
    
    # Example 1
    nums1 = [2, 2, 1]
    assert solution.singleNumber(nums1) == 1, f"Test case 1 failed: {solution.singleNumber(nums1)}"
    print("Test case 1 passed")
    
    # Example 2
    nums2 = [4, 1, 2, 1, 2]
    assert solution.singleNumber(nums2) == 4, f"Test case 2 failed: {solution.singleNumber(nums2)}"
    print("Test case 2 passed")
    
    # Example 3
    nums3 = [1]
    assert solution.singleNumber(nums3) == 1, f"Test case 3 failed: {solution.singleNumber(nums3)}"
    print("Test case 3 passed")
