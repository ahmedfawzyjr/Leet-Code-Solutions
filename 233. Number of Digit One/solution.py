class Solution:
    def countDigitOne(self, n: int) -> int:
        count = 0
        i = 1
        while i <= n:
            divider = i * 10
            count += (n // divider) * i + min(max(n % divider - i + 1, 0), i)
            i *= 10
        return count

if __name__ == "__main__":
    sol = Solution()
    print(f"Count ones in 13: {sol.countDigitOne(13)}") # 6
    print(f"Count ones in 0: {sol.countDigitOne(0)}") # 0
