from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Given an integer array nums, return true if any value appears at least twice in the array,
        and return false if every element is distinct.
        
        We can use a hash set to keep track of the elements we have seen so far.
        If we encounter an element that is already in the set, we return True.
        If we iterate through the entire array without finding any duplicates, we return False.
        
        Time Complexity: O(N)
        Space Complexity: O(N)
        """
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
