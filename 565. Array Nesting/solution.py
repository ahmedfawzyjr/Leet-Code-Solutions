from typing import List

class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        """
        Finds the longest length of a set s[k] built by nesting the array elements.
        
        Complexity:
        - Time: O(N), where N is the length of nums. Each element is visited at most twice.
        - Space: O(1) auxiliary, as we mark visited elements in-place.
        """
        max_len = 0
        n = len(nums)
        
        for i in range(n):
            if nums[i] != -1:
                curr = i
                count = 0
                while nums[curr] != -1:
                    next_val = nums[curr]
                    nums[curr] = -1  # Mark as visited
                    curr = next_val
                    count += 1
                max_len = max(max_len, count)
                
        return max_len
