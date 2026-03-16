from typing import List

class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        distinct_sums = set()
        
        for r in range(m):
            for c in range(n):
                # Rhombus of size 0 (single cell)
                distinct_sums.add(grid[r][c])
                
                # Rhombus of size k > 0
                # Corners: (r-k, c), (r+k, c), (r, c-k), (r, c+k)
                # Limits: r-k >= 0, r+k < m, c-k >= 0, c+k < n
                # So k <= min(r, m-1-r, c, n-1-c)
                max_k = min(r, m-1-r, c, n-1-c)
                for k in range(1, max_k + 1):
                    current_sum = 0
                    
                    # Top corner: (r-k, c)
                    # Bottom corner: (r+k, c)
                    # Left corner: (r, c-k)
                    # Right corner: (r, c+k)
                    
                    # 1. Top to Right side
                    for i in range(k):
                        current_sum += grid[r - k + i][c + i]
                    # 2. Right to Bottom side
                    for i in range(k):
                        current_sum += grid[r + i][c + k - i]
                    # 3. Bottom to Left side
                    for i in range(k):
                        current_sum += grid[r + k - i][c - i]
                    # 4. Left to Top side
                    for i in range(k):
                        current_sum += grid[r - i][c - k + i]
                    
                    distinct_sums.add(current_sum)
                    
        return sorted(list(distinct_sums), reverse=True)[:3]
