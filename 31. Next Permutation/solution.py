from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Rearranges nums into the next lexicographically greater permutation.
        Modifies nums in-place.
        
        Algorithm:
        1. Find the largest index i such that nums[i] < nums[i+1]
        2. Find the largest index j such that nums[i] < nums[j]
        3. Swap nums[i] and nums[j]
        4. Reverse the suffix starting at nums[i+1]
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        n = len(nums)
        
        # Step 1: Find the first decreasing element from the right
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        
        if i >= 0:
            # Step 2: Find the smallest element greater than nums[i] from the right
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            
            # Step 3: Swap nums[i] and nums[j]
            nums[i], nums[j] = nums[j], nums[i]
        
        # Step 4: Reverse the suffix starting at i+1
        left, right = i + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
