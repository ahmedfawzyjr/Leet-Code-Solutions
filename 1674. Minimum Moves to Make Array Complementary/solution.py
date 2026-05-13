from typing import List

class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        """
        To make the array complementary, for every index i, nums[i] + nums[n - 1 - i] must equal some target sum T.
        For each pair (a, b), where a = nums[i] and b = nums[n - 1 - i], let's assume a <= b.
        
        The possible sum T ranges from 2 to 2 * limit.
        Number of moves for a pair (a, b) to reach target sum T:
        - 0 moves: If T == a + b.
        - 1 move: If T is in [min(a, b) + 1, max(a, b) + limit], excluding T == a + b.
        - 2 moves: Otherwise, i.e., T is in [2, min(a, b)] or [max(a, b) + limit + 1, 2 * limit].
        
        We can use a difference array to keep track of the number of moves for each possible sum T.
        """
        n = len(nums)
        # diff array for sums in range [2, 2 * limit]
        # We use size 2 * limit + 2 to handle indices up to 2 * limit + 1
        diff = [0] * (2 * limit + 2)
        
        for i in range(n // 2):
            a, b = nums[i], nums[n - 1 - i]
            if a > b:
                a, b = b, a
            
            # Default to 2 moves for all sums
            diff[2] += 2
            diff[2 * limit + 1] -= 2
            
            # 1 move range: [a + 1, b + limit]
            # Reduce 1 move from the range [a + 1, b + limit]
            diff[a + 1] -= 1
            diff[b + limit + 1] += 1
            
            # 0 moves case: T == a + b
            # Reduce 1 more move for the specific sum a + b
            diff[a + b] -= 1
            diff[a + b + 1] += 1
            
        ans = n
        curr_moves = 0
        for i in range(2, 2 * limit + 1):
            curr_moves += diff[i]
            ans = min(ans, curr_moves)
            
        return ans
