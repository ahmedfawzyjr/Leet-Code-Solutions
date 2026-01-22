class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly = [1]
        i2 = i3 = i5 = 0
        while len(ugly) < n:
            next_ugly = min(ugly[i2] * 2, ugly[i3] * 3, ugly[i5] * 5)
            ugly.append(next_ugly)
            if next_ugly == ugly[i2] * 2:
                i2 += 1
            if next_ugly == ugly[i3] * 3:
                i3 += 1
            if next_ugly == ugly[i5] * 5:
                i5 += 1
        return ugly[n - 1]

if __name__ == "__main__":
    s = Solution()
    test_cases = [
        (10, 12),
        (1, 1),
        (11, 15), # 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15
    ]
    for n, expected in test_cases:
        result = s.nthUglyNumber(n)
        print(f"n={n}, expected={expected}, got={result}, {'PASS' if result == expected else 'FAIL'}")
