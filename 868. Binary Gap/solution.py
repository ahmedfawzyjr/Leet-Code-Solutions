class Solution:
    def binaryGap(self, n: int) -> int:
        last1 = -1
        ans = 0
        pos = 0
        while n > 0:
            if n % 2 == 1:
                if last1 != -1:
                    ans = max(ans, pos - last1)
                last1 = pos
            n //= 2
            pos += 1
        return ans
