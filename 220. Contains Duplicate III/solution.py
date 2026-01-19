from typing import List

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        """
        You are given an integer array nums and two integers indexDiff and valueDiff.
        Find a pair of indices (i, j) such that:
        - i != j,
        - abs(i - j) <= indexDiff.
        - abs(nums[i] - nums[j]) <= valueDiff.
        Return true if such pair exists or false otherwise.
        
        We can use the Bucket Sort concept.
        We place elements into buckets of size w = valueDiff + 1.
        For an element x, its bucket ID is x // w.
        If two numbers are in the same bucket, their difference is at most valueDiff.
        If two numbers are in adjacent buckets, their difference might be at most valueDiff.
        
        We maintain a window of size indexDiff.
        As we iterate, we remove the element that falls out of the window from the buckets.
        
        Time Complexity: O(N)
        Space Complexity: O(min(N, indexDiff))
        """
        if valueDiff < 0:
            return False
            
        buckets = {}
        w = valueDiff + 1
        
        for i, num in enumerate(nums):
            bucket_id = num // w
            
            # Check if current bucket is already occupied
            if bucket_id in buckets:
                return True
            
            # Check adjacent buckets
            if bucket_id - 1 in buckets and abs(num - buckets[bucket_id - 1]) < w:
                return True
            if bucket_id + 1 in buckets and abs(num - buckets[bucket_id + 1]) < w:
                return True
            
            buckets[bucket_id] = num
            
            # Remove element that is out of window
            if i >= indexDiff:
                del buckets[nums[i - indexDiff] // w]
                
        return False
