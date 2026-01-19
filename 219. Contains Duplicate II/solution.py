from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """
        Given an integer array nums and an integer k, return true if there are two distinct indices
        i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
        
        We can use a hash map to store the last seen index of each number.
        As we iterate through the array, if we see a number that is already in the map,
        we check if the difference between the current index and the stored index is <= k.
        If it is, we return True.
        Otherwise, we update the map with the current index (since we want to find the nearest duplicate).
        
        Time Complexity: O(N)
        Space Complexity: O(N)
        """
        index_map = {}
        
        for i, num in enumerate(nums):
            if num in index_map:
                if i - index_map[num] <= k:
                    return True
            index_map[num] = i
            
        return False
