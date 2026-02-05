from typing import List
from collections import Counter

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        """
        Finds the number of tuples (i, j, k, l) such that nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0.
        
        Time complexity: O(n^2) where n is the length of the arrays.
        Space complexity: O(n^2) to store the sums of pairs.
        """
        count = 0
        sum_map = Counter()
        
        # Store all possible sums of pairs from nums1 and nums2
        for a in nums1:
            for b in nums2:
                sum_map[a + b] += 1
                
        # Check if the negation of sums of pairs from nums3 and nums4 exists in sum_map
        for c in nums3:
            for d in nums4:
                target = -(c + d)
                if target in sum_map:
                    count += sum_map[target]
                    
        return count
