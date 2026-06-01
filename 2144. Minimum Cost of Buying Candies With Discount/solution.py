from typing import List

class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        # Sort costs in descending order to get the most expensive candies for free
        cost.sort(reverse=True)
        
        total_cost = 0
        for i in range(len(cost)):
            # Every third candy (indices 2, 5, 8...) is free
            if (i + 1) % 3 != 0:
                total_cost += cost[i]
                
        return total_cost
