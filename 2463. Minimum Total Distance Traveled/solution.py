from typing import List
from functools import lru_cache

class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        """
        Calculates the minimum total distance traveled by all robots to be repaired.
        Using dynamic programming with memoization.
        """
        robot.sort()
        factory.sort()
        
        n = len(robot)
        m = len(factory)
        
        @lru_cache(None)
        def solve(i, j):
            # All robots are repaired
            if i == n:
                return 0
            # No more factories to use but robots remain
            if j == m:
                return float('inf')
            
            # Option 1: Skip factory j
            res = solve(i, j + 1)
            
            # Option 2: Use factory j for k robots (1 <= k <= factory[j][1])
            dist = 0
            limit = factory[j][1]
            pos = factory[j][0]
            
            # Max robots we can repair at factory j is min(limit, remaining robots)
            for k in range(1, min(limit, n - i) + 1):
                dist += abs(robot[i + k - 1] - pos)
                sub_res = solve(i + k, j + 1)
                if sub_res != float('inf'):
                    res = min(res, dist + sub_res)
            
            return res
            
        return solve(0, 0)

if __name__ == "__main__":
    sol = Solution()
    # Example 1
    print(f"Example 1: {sol.minimumTotalDistance([0, 4, 6], [[2, 2], [6, 2]])}")  # Expected: 4
    # Example 2
    print(f"Example 2: {sol.minimumTotalDistance([1, -1], [[-2, 1], [2, 1]])}")   # Expected: 2
