from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Use sets to find the intersection of unique elements
        set1 = set(nums1)
        set2 = set(nums2)
        return list(set1.intersection(set2))
