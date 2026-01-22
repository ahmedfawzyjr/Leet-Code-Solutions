class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        for p in [2, 3, 5]:
            while n % p == 0:
                n //= p
        return n == 1

if __name__ == "__main__":
    s = Solution()
    test_cases = [
        (6, True),
        (1, True),
        (14, False),
        (8, True),
        (0, False),
        (-6, False)
    ]
    for n, expected in test_cases:
        result = s.isUgly(n)
        print(f"n={n}, expected={expected}, got={result}, {'PASS' if result == expected else 'FAIL'}")
