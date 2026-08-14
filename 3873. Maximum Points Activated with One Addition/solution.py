from typing import List
from collections import defaultdict, deque

class Solution:
    def maxActivated(self, points: List[List[int]]) -> int:
        adj = defaultdict(list)
        for x, y in points:
            nx = ('x', x)
            ny = ('y', y)
            adj[nx].append(ny)
            adj[ny].append(nx)
            
        visited = set()
        comp_sizes = []
        
        for node in list(adj.keys()):
            if node not in visited:
                q = deque([node])
                visited.add(node)
                pts_count = 0
                while q:
                    curr = q.popleft()
                    if curr[0] == 'x':
                        pts_count += len(adj[curr])
                    for nxt in adj[curr]:
                        if nxt not in visited:
                            visited.add(nxt)
                            q.append(nxt)
                comp_sizes.append(pts_count)
                
        comp_sizes.sort(reverse=True)
        if len(comp_sizes) == 1:
            return comp_sizes[0] + 1
        else:
            return comp_sizes[0] + comp_sizes[1] + 1
