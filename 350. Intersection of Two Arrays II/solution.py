from typing import List
from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Count frequencies in both arrays
        count1 = Counter(nums1)
        count2 = Counter(nums2)
        
        res = []
        # Find common elements and their minimum frequency
        for num in count1:
            if num in count2:
                res.extend([num] * min(count1[num], count2[num]))
        
        return res
