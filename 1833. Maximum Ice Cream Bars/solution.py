
from typing import List

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        """
        Uses counting sort by price to maximize the number of bars bought.

        Time complexity: O(n + max(costs))
        Space complexity: O(max(costs))
        """
        if not costs:
            return 0

        max_cost = max(costs)
        # Frequency array used for counting sort
        freq = [0] * (max_cost + 1)
        for c in costs:
            freq[c] += 1

        bought = 0
        for price in range(1, max_cost + 1):
            if freq[price] == 0:
                continue

            take = min(freq[price], coins // price)
            bought += take
            coins -= take * price
            if coins == 0:
                break

        return bought
