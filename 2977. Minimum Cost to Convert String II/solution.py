from typing import List
from collections import defaultdict

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        nodes = list(set(original) | set(changed))
        node_to_idx = {node: i for i, node in enumerate(nodes)}
        m = len(nodes)
        
        # dist[i][j] is the min cost to change node i to node j
        dist = [[float('inf')] * m for _ in range(m)]
        for i in range(m):
            dist[i][i] = 0
            
        for u, v, w in zip(original, changed, cost):
            i, j = node_to_idx[u], node_to_idx[v]
            dist[i][j] = min(dist[i][j], w)
            
        # Floyd-Warshall
        for k in range(m):
            for i in range(m):
                if dist[i][k] == float('inf'): continue
                for j in range(m):
                    if dist[k][j] == float('inf'): continue
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
                    
        # Trie to store original strings and their indices
        trie = {}
        for i, node in enumerate(nodes):
            curr = trie
            for char in node:
                if char not in curr:
                    curr[char] = {}
                curr = curr[char]
            curr['#'] = i # Store index of the node
            
        n = len(source)
        dp = [float('inf')] * (n + 1)
        dp[n] = 0
        
        for i in range(n - 1, -1, -1):
            # Option 1: source[i] == target[i], no cost to keep it
            if source[i] == target[i]:
                dp[i] = dp[i+1]
                
            # Option 2: Try all substrings starting at i that match rules
            curr_s = trie
            curr_t = trie
            for j in range(i, n):
                char_s = source[j]
                char_t = target[j]
                
                if char_s not in curr_s or char_t not in curr_t:
                    break
                    
                curr_s = curr_s[char_s]
                curr_t = curr_t[char_t]
                
                if '#' in curr_s and '#' in curr_t:
                    u_idx = curr_s['#']
                    v_idx = curr_t['#']
                    if dist[u_idx][v_idx] != float('inf'):
                        if dist[u_idx][v_idx] + dp[j+1] < dp[i]:
                            dp[i] = dist[u_idx][v_idx] + dp[j+1]
                            # print(f"At i={i}: matched {nodes[u_idx]}->{nodes[v_idx]} (j={j}), new cost={dp[i]}")
                        
        return dp[0] if dp[0] != float('inf') else -1

if __name__ == "__main__":
    sol = Solution()
    
    # Example 1 from image 2977
    source1 = "abcd"
    target1 = "acbe"
    original1 = ["a","b","c","c","e","d"]
    changed1 = ["b","c","b","e","b","e"]
    cost1 = [2,5,5,1,2,20]
    # Path: a->b(2), b->c(5), total a->c = 7. 
    # c->e(1). 
    # d->e(20). 
    # To convert abcd to acbe:
    # a -> a (0) ? No, target[0] is 'a', source[0] is 'a', so keep 'a' (0 cost).
    # b -> c (5)
    # c -> b (5)
    # d -> e (20)
    # Total: 0 + 5 + 5 + 20 = 30? Wait, the image says 28? 
    # Let me re-read the image carefully. 
    # Image says: a->b(2), b->c(5), c->b(5), c->e(1), e->b(2), d->e(20).
    # abcd -> acbe:
    # index 0: 'a' == 'a' (0)
    # index 1: 'b' -> 'c' (5)
    # index 2: 'c' -> 'b' (5)
    # index 3: 'd' -> 'e' (20)
    # Possible better paths?
    # b -> c (5)
    # c -> b: c->e(1) + e->b(2) = 3. 
    # So index 2: c -> b is now 3.
    # Total: 0 + 5 + 3 + 20 = 28. Yes! 28 is correct for THESE rules.
    print(f"Example 1: {sol.minimumCost(source1, target1, original1, changed1, cost1)}") # Expected: 28
    
    # Example 2
    print(f"Example 2: {sol.minimumCost(
        source = "abcdefgh", target = "acdeeghh", 
        original = ["bcd","fgh","thh"], changed = ["cde","thh","ghh"], cost = [1,3,5]
    )}") # Expected: 9
