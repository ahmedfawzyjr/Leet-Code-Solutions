from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones = 0
        twos = 0
        
        for num in nums:
            ones = (ones ^ num) & ~twos
            twos = (twos ^ num) & ~ones
            
        return ones

if __name__ == "__main__":
    solution = Solution()
    
    # Example 1
    nums1 = [2, 2, 3, 2]
    assert solution.singleNumber(nums1) == 3, f"Test case 1 failed: {solution.singleNumber(nums1)}"
    print("Test case 1 passed")
    
    # Example 2
    nums2 = [0, 1, 0, 1, 0, 1, 99]
    assert solution.singleNumber(nums2) == 99, f"Test case 2 failed: {solution.singleNumber(nums2)}"
    print("Test case 2 passed")
