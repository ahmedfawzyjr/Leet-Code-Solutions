
from typing import List

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        if not costs:
            return 0
        max_cost = max(costs)
        # Create frequency array for counting sort
        freq = [0] * (max_cost + 1)
        for c in costs:
            freq[c] += 1
        res = 0
        for cost in range(1, max_cost + 1):
            if freq[cost] == 0:
                continue
            # How many can we buy of this cost
            take = min(freq[cost], coins // cost)
            res += take
            coins -= take * cost
            if coins == 0:
                break
        return res
