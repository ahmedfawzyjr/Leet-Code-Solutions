from typing import List

class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        m = len(grid[0])
        total_elements = n * m
        
        pref = [1] * total_elements
        suff = [1] * total_elements
        
        flat_grid = []
        for i in range(n):
            for j in range(m):
                flat_grid.append(grid[i][j] % 12345)
                
        # Fill prefix
        curr = 1
        for i in range(total_elements):
            pref[i] = curr
            curr = (curr * flat_grid[i]) % 12345
            
        # Fill suffix
        curr = 1
        for i in range(total_elements - 1, -1, -1):
            suff[i] = curr
            curr = (curr * flat_grid[i]) % 12345
            
        res = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                idx = i * m + j
                res[i][j] = (pref[idx] * suff[idx]) % 12345
                
        return res
