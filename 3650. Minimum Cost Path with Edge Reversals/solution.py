import heapq
from typing import List

class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            # Normal edge
            adj[u].append((v, w))
            # Reversed edge (using switch at u)
            adj[u].append((v, 2 * w, True))
            
        # State: (cost, node, switch_used_at_this_node)
        # Wait, as analyzed, the "at most once" per node is naturally handled
        # because cycles are not optimal with positive weights.
        # However, we must ensure we don't use the switch at the same node twice
        # in the SAME path. But we only leave a node once in a simple path.
        
        # Actually, the problem says "when you arrive at u_i ... you may activate it".
        # This means the switch is at u_i.
        # Let's refine the graph:
        # For each edge u -> v with weight w:
        # 1. u -> v (weight w) - normal traversal
        # 2. v -> u (weight 2w) - using switch at v to go to u
        
        refined_adj = [[] for _ in range(n)]
        for u, v, w in edges:
            refined_adj[u].append((v, w))
            refined_adj[v].append((u, 2 * w))
            
        dist = [float('inf')] * n
        dist[0] = 0
        pq = [(0, 0)]
        
        while pq:
            d, u = heapq.heappop(pq)
            
            if d > dist[u]:
                continue
            
            if u == n - 1:
                return d
                
            for v, w in refined_adj[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    heapq.heappush(pq, (dist[v], v))
                    
        return dist[n-1] if dist[n-1] != float('inf') else -1

if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    n1 = 4
    edges1 = [[0,1,3], [3,1,1], [2,3,4], [0,2,2]]
    print(f"Example 1: {sol.minCost(n1, edges1)}") # Expected: 5
    
    # Example 2
    n2 = 4
    edges2 = [[0,2,1], [2,1,1], [1,3,1], [2,3,3]]
    print(f"Example 2: {sol.minCost(n2, edges2)}") # Expected: 3
