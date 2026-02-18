class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        # XOR n with n shifted right by 1.
        # If n has alternating bits, then n ^ (n >> 1) will be all 1s.
        x = n ^ (n >> 1)
        
        # Check if x is all 1s.
        # If x is all 1s, then x & (x + 1) should be 0.
        return (x & (x + 1)) == 0
