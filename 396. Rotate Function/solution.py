from typing import List

class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = sum(nums)
        f = sum(i * num for i, num in enumerate(nums))
        max_val = f
        
        for i in range(1, n):
            f = f + total_sum - n * nums[n-i]
            max_val = max(max_val, f)
            
        return max_val

if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    nums1 = [4,3,2,6]
    print(f"Test 1: {sol.maxRotateFunction(nums1)} (Expected: 26)")
    
    # Example 2
    nums2 = [100]
    print(f"Test 2: {sol.maxRotateFunction(nums2)} (Expected: 0)")

