from typing import List

class Solution:
    def check(self, nums: List[int]) -> bool:
        """
        An array is sorted and rotated if there is at most one index i such that 
        nums[i] > nums[(i + 1) % n].
        
        Complexity:
        - Time: O(N) where N is the length of the array.
        - Space: O(1).
        """
        count = 0
        n = len(nums)
        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                count += 1
                
        return count <= 1
