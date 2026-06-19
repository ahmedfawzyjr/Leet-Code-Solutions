
from typing import List
import collections

class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m, n = len(matrix), len(matrix[0])
        # Compute prefix sums row-wise
        for row in matrix:
            for j in range(1, n):
                row[j] += row[j-1]
        res = 0
        # Iterate over left boundary
        for left in range(n):
            # Initialize row-wise sum array
            row_sum = [0] * m
            for right in range(left, n):
                # Update row_sum for this right boundary
                for i in range(m):
                    if left == 0:
                        row_sum[i] = matrix[i][right]
                    else:
                        row_sum[i] = matrix[i][right] - matrix[i][left-1]
                # Now compute subarray sum target using hash map
                prefix_map = collections.defaultdict(int)
                prefix_map[0] = 1
                current = 0
                for num in row_sum:
                    current += num
                    if current - target in prefix_map:
                        res += prefix_map[current - target]
                    prefix_map[current] += 1
        return res
