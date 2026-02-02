from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        
        m, n = len(heights), len(heights[0])
        pacific = [[False] * n for _ in range(m)]
        atlantic = [[False] * n for _ in range(m)]
        
        def dfs(r, c, reachable, prev_height):
            if (r < 0 or r >= m or c < 0 or c >= n or 
                reachable[r][c] or heights[r][c] < prev_height):
                return
            
            reachable[r][c] = True
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                dfs(r + dr, c + dc, reachable, heights[r][c])
        
        for i in range(m):
            dfs(i, 0, pacific, heights[i][0])
            dfs(i, n - 1, atlantic, heights[i][n - 1])
            
        for j in range(n):
            dfs(0, j, pacific, heights[0][j])
            dfs(m - 1, j, atlantic, heights[m - 1][j])
            
        res = []
        for i in range(m):
            for j in range(n):
                if pacific[i][j] and atlantic[i][j]:
                    res.append([i, j])
                    
        return res
