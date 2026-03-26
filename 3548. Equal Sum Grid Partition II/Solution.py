from typing import List

class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        
        rowSum = [sum(row) for row in grid]
        colSum = [sum(grid[r][c] for r in range(m)) for c in range(n)]
        
        totalSum = sum(rowSum)
        
        def check_section(r1, r2, c1, c2, target):
            R = r2 - r1 + 1
            C = c2 - c1 + 1
            
            # Special case for discounting the ONLY cell in a 1x1 section
            if R == 1 and C == 1:
                return grid[r1][c1] == target
            
            # Connectivity rule:
            # - If R > 1 and C > 1, removing any single cell leaves it connected.
            # - If R == 1 and C > 1, removing a cell leaves it connected only if it's an endpoint.
            # - If C == 1 and R > 1, removing a cell leaves it connected only if it's an endpoint.
            
            if R > 1 and C > 1:
                for r in range(r1, r2 + 1):
                    for c in range(c1, c2 + 1):
                        if grid[r][c] == target:
                            return True
            elif R == 1: # and C > 1
                if grid[r1][c1] == target or grid[r1][c2] == target:
                    return True
            elif C == 1: # and R > 1
                if grid[r1][c1] == target or grid[r2][c1] == target:
                    return True
            return False

        # Horizontal cuts
        s1 = 0
        for r in range(m - 1):
            s1 += rowSum[r]
            s2 = totalSum - s1
            if s1 == s2:
                return True
            if s1 > s2:
                if check_section(0, r, 0, n - 1, s1 - s2):
                    return True
            else: # s2 > s1
                if check_section(r + 1, m - 1, 0, n - 1, s2 - s1):
                    return True
                    
        # Vertical cuts
        s_left = 0
        for c in range(n - 1):
            s_left += colSum[c]
            s_right = totalSum - s_left
            if s_left == s_right:
                return True
            if s_left > s_right:
                if check_section(0, m - 1, 0, c, s_left - s_right):
                    return True
            else: # s_right > s_left
                if check_section(0, m - 1, c + 1, n - 1, s_right - s_left):
                    return True
        
        return False
