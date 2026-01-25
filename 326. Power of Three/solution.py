class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # The maximum power of 3 that fits in a 32-bit signed integer is 3^19 = 1162261467
        return n > 0 and 1162261467 % n == 0
