import collections

class Solution:
    def shortestDistance(self, grid: list[list[int]]) -> int:
        if not grid or not grid[0]:
            return -1
        
        rows, cols = len(grid), len(grid[0])
        dist_sum = [[0] * cols for _ in range(rows)]
        walkable_value = 0
        min_dist = float('inf')
        
        buildings = []
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    buildings.append((r, c))
        
        for br, bc in buildings:
            min_dist = float('inf')
            queue = collections.deque([(br, bc, 0)])
            
            while queue:
                r, c, d = queue.popleft()
                
                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nr, nc = r + dr, c + dc
                    
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == walkable_value:
                        grid[nr][nc] -= 1
                        dist_sum[nr][nc] += d + 1
                        queue.append((nr, nc, d + 1))
                        min_dist = min(min_dist, dist_sum[nr][nc])
            
            walkable_value -= 1
            if min_dist == float('inf'):
                return -1
                
        return min_dist if min_dist != float('inf') else -1
