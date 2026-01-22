import math

class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        
        for i in range(1, n + 1):
            j = 1
            while j * j <= i:
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1
                
        return dp[n]

if __name__ == "__main__":
    s = Solution()
    test_cases = [
        (12, 3),
        (13, 2),
        (1, 1),
        (4, 1)
    ]
    for n, expected in test_cases:
        result = s.numSquares(n)
        print(f"n={n}, expected={expected}, got={result}, {'PASS' if result == expected else 'FAIL'}")
