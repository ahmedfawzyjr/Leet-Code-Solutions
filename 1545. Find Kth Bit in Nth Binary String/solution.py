class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if n == 1:
            return "0"
        
        length = (1 << n) - 1
        mid = (length >> 1) + 1
        
        if k == mid:
            return "1"
        elif k < mid:
            return self.findKthBit(n - 1, k)
        else:
            # k > mid
            # The bit is invert(S_{n-1}[2^n - k])
            bit = self.findKthBit(n - 1, (1 << n) - k)
            return "1" if bit == "0" else "0"
