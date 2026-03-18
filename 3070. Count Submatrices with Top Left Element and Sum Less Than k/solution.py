from typing import List

class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        pref = [[0] * (n + 1) for _ in range(m + 1)]
        count = 0
        
        for r in range(m):
            for c in range(n):
                pref[r + 1][c + 1] = grid[r][c] + pref[r][c + 1] + pref[r + 1][c] - pref[r][c]
                if pref[r + 1][c + 1] <= k:
                    count += 1
                else:
                    # Since grid values are non-negative, if prefix sum exceeds k, 
                    # all larger submatrices starting from the same (0,0) will also exceed k.
                    # However, we only know that pref[r+1][c'+1] for c' > c will exceed k.
                    # We can break the inner loop early.
                    break
        return count
