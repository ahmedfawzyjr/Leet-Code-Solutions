from typing import List

class Solution:
    def minimumFlips(self, n: int, edges: List[List[int]], start: str, target: str) -> List[int]:
        need_flip = [int(s != t) for s, t in zip(start, target)]
        if sum(need_flip) % 2 != 0:
            return [-1]
        
        adj = [[] for _ in range(n)]
        for i, (u, v) in enumerate(edges):
            adj[u].append((v, i))
            adj[v].append((u, i))
            
        parent = [-1] * n
        parent_edge = [-1] * n
        order = []
        visited = [False] * n
        queue = [0]
        visited[0] = True
        q_idx = 0
        
        while q_idx < len(queue):
            curr = queue[q_idx]
            q_idx += 1
            order.append(curr)
            for nbr, edge_idx in adj[curr]:
                if not visited[nbr]:
                    visited[nbr] = True
                    parent[nbr] = curr
                    parent_edge[nbr] = edge_idx
                    queue.append(nbr)
                    
        toggled_edges = []
        for u in reversed(order):
            if u == 0:
                continue
            if need_flip[u]:
                p = parent[u]
                e_idx = parent_edge[u]
                toggled_edges.append(e_idx)
                need_flip[p] ^= 1
                need_flip[u] ^= 1
                
        toggled_edges.sort()
        return toggled_edges
