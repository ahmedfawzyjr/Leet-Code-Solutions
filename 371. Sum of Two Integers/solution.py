class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 32-bit integer max
        MAX = 0x7FFFFFFF
        # 32-bit integer mask
        mask = 0xFFFFFFFF
        
        while b != 0:
            # a ^ b handles sum without carry
            # (a & b) << 1 handles carry
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
            
        # If a is negative in 32-bit sense, return it as negative in Python
        return a if a <= MAX else ~(a ^ mask)
