class Solution:
    def integerBreak(self, n: int) -> int:
        # Base cases for n = 2 and n = 3
        if n == 2:
            return 1
        if n == 3:
            return 2
        
        # For n > 3, we want to use as many 3s as possible.
        # If the remainder is 1, we use (3 * 3 ... * 3 * 4) instead of (3 * 3 ... * 3 * 1)
        # If the remainder is 2, we use (3 * 3 ... * 3 * 2)
        # If the remainder is 0, we use (3 * 3 ... * 3)
        
        res = 1
        while n > 4:
            res *= 3
            n -= 3
        
        return res * n
