
from solution import Solution

sol = Solution()

print("count_waviness(4847):", sol._Solution__count_waviness(4847) if hasattr(sol, '_Solution__count_waviness') else "Wait let's rewrite")

# Let's reimplement count_waviness here for debugging
from functools import lru_cache

def count_waviness(x):
    if x < 100:
        return 0
    s = list(map(int, str(x)))
    n = len(s)
    
    @lru_cache(maxsize=None)
    def dp(pos, prev1, prev2, tight, leading_zero):
        if pos == n:
            return 0
        res = 0
        upper = s[pos] if tight else 9
        for d in range(0, upper + 1):
            new_tight = tight and (d == upper)
            new_leading_zero = leading_zero and (d == 0)
            if new_leading_zero:
                res += dp(pos + 1, -1, -1, new_tight, new_leading_zero)
            else:
                if prev2 == -1:
                    res += dp(pos + 1, d, prev1, new_tight, new_leading_zero)
                else:
                    add = 0
                    if (prev1 > prev2 and prev1 > d) or (prev1 < prev2 and prev1 < d):
                        add = 1
                    res += add + dp(pos + 1, d, prev1, new_tight, new_leading_zero)
        return res
    
    return dp(0, -1, -1, True, True)

print("count_waviness(4847):", count_waviness(4847))
print("count_waviness(4848):", count_waviness(4848))
print("difference:", count_waviness(4848) - count_waviness(4847))
