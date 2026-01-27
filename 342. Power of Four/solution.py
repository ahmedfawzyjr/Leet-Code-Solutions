class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # A number n is a power of four if:
        # 1. n > 0
        # 2. n is a power of two: n & (n - 1) == 0
        # 3. (n - 1) is divisible by 3: (n - 1) % 3 == 0
        #    Alternatively: n % 3 == 1
        return n > 0 and (n & (n - 1)) == 0 and n % 3 == 1
