from collections import deque
from typing import List

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank_set = set(bank)
        if endGene not in bank_set:
            return -1
        
        queue = deque([(startGene, 0)])
        visited = {startGene}
        
        while queue:
            curr, dist = queue.popleft()
            if curr == endGene:
                return dist
            
            for i in range(len(curr)):
                for char in "ACGT":
                    mutation = curr[:i] + char + curr[i+1:]
                    if mutation in bank_set and mutation not in visited:
                        visited.add(mutation)
                        queue.append((mutation, dist + 1))
        
        return -1
