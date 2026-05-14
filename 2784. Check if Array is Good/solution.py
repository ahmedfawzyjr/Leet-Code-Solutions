from typing import List

class Solution:
    def isGood(self, nums: List[int]) -> bool:
        """
        An array is good if it is a permutation of base[n] = [1, 2, ..., n-1, n, n],
        where n is the maximum element in the array.
        
        Logic:
        1. Let n = len(nums) - 1.
        2. A good array of length n + 1 must contain numbers from 1 to n-1 once and n twice.
        3. Sorting the array and comparing it with the expected base[n] is an efficient check.
        """
        n = len(nums) - 1
        if n < 1:
            return False
        
        # Construct the base[n] array and compare with sorted nums
        expected = list(range(1, n)) + [n, n]
        return sorted(nums) == expected
