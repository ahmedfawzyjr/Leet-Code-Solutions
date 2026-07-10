from typing import List
from collections import defaultdict

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
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
                if root_i == find(0):
                    parent[root_j] = root_i
                else:
                    parent[root_i] = root_j

        # Initially, person 0 and firstPerson share the secret
        union(0, firstPerson)
        
        # Group meetings by time
        meetings_by_time = defaultdict(list)
        for x, y, t in meetings:
            meetings_by_time[t].append((x, y))
            
        # Process meetings chronologically
        for t in sorted(meetings_by_time.keys()):
            people = set()
            for x, y in meetings_by_time[t]:
                union(x, y)
                people.add(x)
                people.add(y)
                
            # Reset people who did not get the secret
            secret_root = find(0)
            for p in people:
                if find(p) != secret_root:
                    parent[p] = p
                    
        # Collect everyone who knows the secret
        secret_root = find(0)
        return [i for i in range(n) if find(i) == secret_root]
