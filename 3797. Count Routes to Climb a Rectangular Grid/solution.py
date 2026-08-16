import math
from typing import List

class Solution:
    def numberOfRoutes(self, grid: List[str], d: int) -> int:
        m = len(grid)
        n = len(grid[0])
        MOD = 10**9 + 7
        
        # dp_from_below[c]: number of valid routes that reach (r, c) by a vertical step from row r + 1
        # (or routes consisting only of starting at (m - 1, c))
        dp_from_below = [0] * n
        for c in range(n):
            if grid[m - 1][c] == '.':
                dp_from_below[c] = 1
                
        for r in range(m - 1, -1, -1):
            # 1. Compute dp_current_cell[c]: routes ending at (r, c) that are ready to move to row r - 1 (or finish if r == 0)
            dp_current_cell = [0] * n
            
            # Prefix sums of dp_from_below for fast range sum queries
            pref_from_below = [0] * (n + 1)
            for c in range(n):
                pref_from_below[c + 1] = (pref_from_below[c] + dp_from_below[c]) % MOD
                
            for c in range(n):
                if grid[r][c] == '.':
                    L = max(0, c - d)
                    R = min(n - 1, c + d)
                    # Sum of dp_from_below[k] for k != c such that |k - c| <= d
                    ways_from_other_cols = (pref_from_below[R + 1] - pref_from_below[L] - dp_from_below[c]) % MOD
                    dp_current_cell[c] = (dp_from_below[c] + ways_from_other_cols) % MOD
                    
            if r == 0:
                return sum(dp_current_cell) % MOD
                
            # 2. Compute dp_from_below for row r - 1: moving from row r to row r - 1
            next_dp_from_below = [0] * n
            
            if d >= 1:
                d_col_max = math.isqrt(d * d - 1)
                pref_current = [0] * (n + 1)
                for c in range(n):
                    pref_current[c + 1] = (pref_current[c] + dp_current_cell[c]) % MOD
                    
                for c_up in range(n):
                    if grid[r - 1][c_up] == '.':
                        L = max(0, c_up - d_col_max)
                        R = min(n - 1, c_up + d_col_max)
                        next_dp_from_below[c_up] = (pref_current[R + 1] - pref_current[L]) % MOD
                        
            dp_from_below = next_dp_from_below
            
        return 0
