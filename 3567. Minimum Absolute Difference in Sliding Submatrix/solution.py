from typing import List

class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        res_m = m - k + 1
        res_n = n - k + 1
        res = [[0] * res_n for _ in range(res_m)]
        
        for i in range(res_m):
            for j in range(res_n):
                # Extract the k x k submatrix elements
                elements = []
                for r in range(i, i + k):
                    for c in range(j, j + k):
                        elements.append(grid[r][c])
                
                # Use a set to get distinct values
                distinct_values = sorted(list(set(elements)))
                
                if len(distinct_values) <= 1:
                    res[i][j] = 0
                else:
                    # Find minimum difference between adjacent sorted distinct elements
                    min_diff = float('inf')
                    for idx in range(len(distinct_values) - 1):
                        diff = distinct_values[idx+1] - distinct_values[idx]
                        if diff < min_diff:
                            min_diff = diff
                    res[i][j] = min_diff
                    
        return res
