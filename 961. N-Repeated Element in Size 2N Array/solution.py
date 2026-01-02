from typing import List


class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        """
        Find the element that is repeated n times in a 2n-sized array.
        
        Since the array has 2n elements with n+1 unique elements,
        and one element is repeated n times, we can use a set to
        detect the first duplicate.
        
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        seen = set()
        
        for num in nums:
            if num in seen:
                return num
            seen.add(num)
        
        return -1  # Should never reach here given problem constraints
