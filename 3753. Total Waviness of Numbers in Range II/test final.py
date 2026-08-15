
from solution import Solution
from functools import lru_cache

def brute_waviness(x):
    s = list(map(int, str(x)))
    if len(s) < 3:
        return 0
    res = 0
    for i in range(1, len(s)-1):
        prev = s[i-1]
        curr = s[i]
        next_d = s[i+1]
        if (curr > prev and curr > next_d) or (curr < prev and curr < next_d):
            res += 1
    return res

def count_waviness_brute(x):
    total = 0
    for i in range(1, x+1):
        total += brute_waviness(i)
    return total

sol = Solution()

# Test examples from problem
print("Test 1 (120-130):", sol.totalWaviness(120, 130))  # Should be 3
print("Test 2 (198-202):", sol.totalWaviness(198, 202))  # Should be 3
print("Test 3 (4848-4848):", sol.totalWaviness(4848, 4848))  # Should be 2

# Verify no discrepancies up to 2000
print("\nVerifying up to 2000...")
all_good = True
for x in range(1, 2001):
    dp = sol.count_waviness(x)
    brute = count_waviness_brute(x)
    if dp != brute:
        print(f"Discrepancy at x={x}: dp={dp}, brute={brute}")
        all_good = False
        break
if all_good:
    print("All tests up to 2000 passed!")
