class Solution:
    def concatenatedBinary(self, n: int) -> int:
        MOD = 10**9 + 7
        ans = 0
        length = 0
        
        for i in range(1, n + 1):
            # If `i` is a power of 2, its binary representation has one more bit
            if i & (i - 1) == 0:
                length += 1
            
            # Shift the current answer by `length` bits to the left and add `i`
            ans = ((ans << length) | i) % MOD
            
        return ans
