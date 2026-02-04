import math

class Solution:
    def arrangeCoins(self, n: int) -> int:
        # k(k+1)/2 <= n
        # k^2 + k - 2n <= 0
        # k = (-1 + sqrt(1 + 8n)) / 2
        return int((-1 + math.sqrt(1 + 8 * n)) / 2)
