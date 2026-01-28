from typing import List
import bisect

class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        rows, cols = len(matrix), len(matrix[0])
        res = float('-inf')
        
        for left in range(cols):
            row_sums = [0] * rows
            for right in range(left, cols):
                for i in range(rows):
                    row_sums[i] += matrix[i][right]
                
                # Find max subarray sum no larger than k
                # This is equivalent to finding max(prefix_sum[j] - prefix_sum[i]) <= k
                # prefix_sum[j] - k <= prefix_sum[i]
                
                sorted_prefix_sums = [0]
                curr_sum = 0
                for s in row_sums:
                    curr_sum += s
                    idx = bisect.bisect_left(sorted_prefix_sums, curr_sum - k)
                    if idx < len(sorted_prefix_sums):
                        res = max(res, curr_sum - sorted_prefix_sums[idx])
                    bisect.insort(sorted_prefix_sums, curr_sum)
                    
        return res
