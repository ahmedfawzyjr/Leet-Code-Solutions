from typing import List
from bisect import bisect_left

class Solution:
    def closestEqualElement(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        # Map each value to a sorted list of its indices
        indices_map = {}
        for idx, val in enumerate(nums):
            if val not in indices_map:
                indices_map[val] = []
            indices_map[val].append(idx)
        
        results = []
        for q_idx in queries:
            target_val = nums[q_idx]
            idx_list = indices_map[target_val]
            
            if len(idx_list) == 1:
                results.append(-1)
                continue
            
            # Find the position of q_idx in idx_list
            pos = bisect_left(idx_list, q_idx)
            
            # Neighbors are at (pos-1) and (pos+1) with wrap-around
            left_neighbor = idx_list[(pos - 1) % len(idx_list)]
            right_neighbor = idx_list[(pos + 1) % len(idx_list)]
            
            # Circular distance formula: min(|i-j|, n - |i-j|)
            def circular_dist(i, j):
                abs_diff = abs(i - j)
                return min(abs_diff, n - abs_diff)
            
            dist_left = circular_dist(q_idx, left_neighbor)
            dist_right = circular_dist(q_idx, right_neighbor)
            
            results.append(min(dist_left, dist_right))
            
        return results
