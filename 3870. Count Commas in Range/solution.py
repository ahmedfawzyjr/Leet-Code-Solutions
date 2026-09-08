class Solution:
    def countCommas(self, n: int) -> int:
        count = 0
        p = 1000
        while p <= n:
            count += n - p + 1
            p *= 1000
        return count

if __name__ == "__main__":
    sol = Solution()
    print(sol.countCommas(1002)) # Expected: 3
    print(sol.countCommas(998))  # Expected: 0
    print(sol.countCommas(100000)) # Expected: 100000 - 1000 + 1 = 99001
