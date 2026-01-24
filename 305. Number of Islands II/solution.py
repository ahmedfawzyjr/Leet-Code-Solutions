from typing import List

class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        parent = {}
        def find(i):
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])
            return parent[i]
            
        def union(i, j):
            root_i = find(i)
            root_j = find(j)
            if root_i != root_j:
                parent[root_i] = root_j
                return True
            return False
            
        res = []
        count = 0
        grid = set()
        for r, c in positions:
            if (r, c) in grid:
                res.append(count)
                continue
            
            grid.add((r, c))
            parent[(r, c)] = (r, c)
            count += 1
            
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if (nr, nc) in grid:
                    if union((r, c), (nr, nc)):
                        count -= 1
            res.append(count)
        return res
