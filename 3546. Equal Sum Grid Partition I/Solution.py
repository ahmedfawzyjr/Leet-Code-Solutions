from typing import List

class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        m = len(grid[0])
        
        # Calculate row sums
        row_sums = [sum(row) for row in grid]
        total_sum = sum(row_sums)
        
        # Total sum must be even for a 50/50 split
        if total_sum % 2 != 0:
            return False
        
        target = total_sum // 2
        
        # Check horizontal cuts (between rows)
        curr_row_sum = 0
        for i in range(n - 1): # Cut after row i, so i+1 rows in the first part
            curr_row_sum += row_sums[i]
            if curr_row_sum == target:
                return True
                
        # Check vertical cuts (between columns)
        # Calculate column sums
        col_sums = [0] * m
        for j in range(m):
            for i in range(n):
                col_sums[j] += grid[i][j]
                
        curr_col_sum = 0
        for j in range(m - 1): # Cut after column j, so j+1 columns in the first part
            curr_col_sum += col_sums[j]
            if curr_col_sum == target:
                return True
                
        return False
