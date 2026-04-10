from typing import List
from collections import defaultdict

class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        indices = defaultdict(list)
        for i, num in enumerate(nums):
            indices[num].append(i)
        
        min_dist = 10**18
        found = False
        
        for num in indices:
            idx_list = indices[num]
            if len(idx_list) >= 3:
                found = True
                for i in range(len(idx_list) - 2):
                    # Distance is abs(i-j) + abs(j-k) + abs(k-i)
                    # For sorted indices i < j < k: (j-i) + (k-j) + (k-i) = 2*(k-i)
                    dist = 2 * (idx_list[i+2] - idx_list[i])
                    if dist < min_dist:
                        min_dist = dist
        
        return int(min_dist) if found else -1
