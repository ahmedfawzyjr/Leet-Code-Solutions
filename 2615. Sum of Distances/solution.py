from typing import List
from collections import defaultdict

class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        # Group indices by their values
        d = defaultdict(list)
        for i, val in enumerate(nums):
            d[val].append(i)
        
        # For each value, calculate the sum of distances for each index
        for val, indices in d.items():
            k = len(indices)
            if k == 1:
                continue
            
            # Total sum of all indices for this value
            total_sum = sum(indices)
            # Prefix sum of indices encountered so far
            prefix_sum = 0
            
            for i, idx in enumerate(indices):
                # Using the formula: (i * idx - prefix_sum) + ((total_sum - prefix_sum - idx) - (k - 1 - i) * idx)
                # Left side: sum of distances from current index to all indices before it
                left_dist = i * idx - prefix_sum
                # Right side: sum of distances from current index to all indices after it
                right_dist = (total_sum - prefix_sum - idx) - (k - 1 - i) * idx
                res[idx] = left_dist + right_dist
                prefix_sum += idx
                
        return res
