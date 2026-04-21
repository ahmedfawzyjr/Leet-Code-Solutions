from typing import List
from collections import defaultdict, Counter

class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        parent = list(range(n))
        
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
                
        for a, b in allowedSwaps:
            union(a, b)
            
        components = defaultdict(list)
        for i in range(n):
            components[find(i)].append(i)
            
        matches = 0
        for indices in components.values():
            source_counts = Counter()
            target_counts = Counter()
            for i in indices:
                source_counts[source[i]] += 1
                target_counts[target[i]] += 1
            
            for val, count in source_counts.items():
                if val in target_counts:
                    matches += min(count, target_counts[val])
                    
        return n - matches
