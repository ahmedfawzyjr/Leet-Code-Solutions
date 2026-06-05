
from functools import lru_cache

def brute_waviness(x):
    s = list(map(int, str(x)))
    if len(s) < 3:
        return 0
    res =0
    for i in range(1, len(s)-1):
        prev = s[i-1]
        curr = s[i]
        next_d = s[i+1]
        if (curr > prev and curr > next_d) or (curr < prev and curr < next_d):
            res +=1
    return res

def count_waviness_brute(x):
    total = 0
    for i in range(1, x+1):
        total += brute_waviness(i)
    return total

def count_waviness_dp(x):
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

for x in range(1001, 1012):
    dp_prev = count_waviness_dp(x-1)
    dp_curr = count_waviness_dp(x)
    delta_dp = dp_curr - dp_prev
    delta_brute = brute_waviness(x)
    print(f"x={x}: delta_dp={delta_dp}, delta_brute={delta_brute}")
