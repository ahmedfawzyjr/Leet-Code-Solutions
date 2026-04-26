from typing import List

class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        rows = len(grid)
        cols = len(grid[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        
        def dfs(r, c, pr, pc, char):
            visited[r][c] = True
            
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == char:
                    if visited[nr][nc]:
                        # If the neighbor is visited and it's not the immediate parent, we found a cycle
                        if (nr, nc) != (pr, pc):
                            return True
                    else:
                        if dfs(nr, nc, r, c, char):
                            return True
            return False

        for r in range(rows):
            for c in range(cols):
                if not visited[r][c]:
                    if dfs(r, c, -1, -1, grid[r][c]):
                        return True
        return False
