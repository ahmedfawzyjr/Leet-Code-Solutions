from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        
        def reverse(start: int, end: int) -> None:
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        
        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)

if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    nums1 = [1, 2, 3, 4, 5, 6, 7]
    k1 = 3
    sol.rotate(nums1, k1)
    print(f"Example 1 Output: {nums1}")
    # Expected: [5, 6, 7, 1, 2, 3, 4]
    
    # Example 2
    nums2 = [-1, -100, 3, 99]
    k2 = 2
    sol.rotate(nums2, k2)
    print(f"Example 2 Output: {nums2}")
    # Expected: [3, 99, -1, -100]
