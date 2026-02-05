from typing import List

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        """
        Returns the minimum number of moves required to make all array elements equal.
        Incrementing n-1 elements by 1 is equivalent to decrementing 1 element by 1.
        
        Time complexity: O(n)
        Space complexity: O(1)
        """
        min_val = min(nums)
        return sum(nums) - len(nums) * min_val
