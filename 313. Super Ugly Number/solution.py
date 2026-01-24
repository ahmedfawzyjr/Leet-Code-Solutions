import heapq
from typing import List

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        uglies = [1]
        # (value, prime, index_in_uglies)
        heap = [(p, p, 0) for p in primes]
        heapq.heapify(heap)
        
        while len(uglies) < n:
            val, p, idx = heap[0]
            if val > uglies[-1]:
                uglies.append(val)
            
            # Update the heap with the next multiple for this prime
            new_val = uglies[idx + 1] * p
            heapq.heapreplace(heap, (new_val, p, idx + 1))
            
        return uglies[-1]
