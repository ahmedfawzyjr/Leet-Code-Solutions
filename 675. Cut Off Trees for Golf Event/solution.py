
from typing import List
from collections import deque

class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        if not forest or not forest[0]:
            return 0
        
        m, n = len(forest), len(forest[0])
        trees = []
        for i in range(m):
            for j in range(n):
                if forest[i][j] > 1:
                    trees.append((forest[i][j], i, j))
        trees.sort()
        
        total_steps = 0
        start_x, start_y = 0, 0
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        def bfs(sx, sy, ex, ey):
            if sx == ex and sy == ey:
                return 0
            visited = [[False]*n for _ in range(m)]
            q = deque()
            q.append((sx, sy))
            visited[sx][sy] = True
            steps = 0
            while q:
                level_size = len(q)
                steps += 1
                for _ in range(level_size):
                    x, y = q.popleft()
                    for dx, dy in directions:
                        nx = x + dx
                        ny = y + dy
                        if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and forest[nx][ny] != 0:
                            if nx == ex and ny == ey:
                                return steps
                            visited[nx][ny] = True
                            q.append((nx, ny))
            return -1
        
        for _, x, y in trees:
            steps = bfs(start_x, start_y, x, y)
            if steps == -1:
                return -1
            total_steps += steps
            start_x, start_y = x, y
        
        return total_steps
