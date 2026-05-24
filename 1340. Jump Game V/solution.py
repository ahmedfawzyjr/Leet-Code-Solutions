from typing import List

class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        """
        Calculates the maximum number of indices that can be visited starting 
        from any index using DP with memoization.
        
        Complexity:
        - Time: O(N * d) where N is the length of the array and d is the jump distance.
        - Space: O(N) for the memoization table and recursion stack.
        """
        n = len(arr)
        memo = [-1] * n
        
        def solve(i: int) -> int:
            if memo[i] != -1:
                return memo[i]
            
            res = 1
            
            # Jump to the right
            for j in range(i + 1, min(i + d + 1, n)):
                if arr[j] < arr[i]:
                    res = max(res, 1 + solve(j))
                else:
                    # All indices between i and j must be smaller than arr[i]
                    break
            
            # Jump to the left
            for j in range(i - 1, max(i - d - 1, -1), -1):
                if arr[j] < arr[i]:
                    res = max(res, 1 + solve(j))
                else:
                    break
            
            memo[i] = res
            return res
        
        return max(solve(i) for i in range(n))
