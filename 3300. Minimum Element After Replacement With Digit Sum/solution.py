from typing import List

class Solution:
    def minElement(self, nums: List[int]) -> int:
        """
        Replaces each element in nums with the sum of its digits and returns the minimum.
        
        Complexity:
        - Time: O(N * log10(M)) where N is the length of nums and M is the maximum value in nums.
        - Space: O(1) as we calculate the minimum in one pass.
        """
        def digit_sum(n: int) -> int:
            s = 0
            while n > 0:
                s += n % 10
                n //= 10
            return s
            
        return min(digit_sum(num) for num in nums)
