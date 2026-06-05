
from functools import lru_cache

def count_waviness(x):
    if x < 100:
        return 0
    s = list(map(int, str(x)))
    n = len(s)
    print("Processing", x, "digits:", s)
    
    @lru_cache(maxsize=None)
    def dp(pos, prev1, prev2, tight, leading_zero):
        if pos == n:
            print(f"  dp({pos}, {prev1}, {prev2}, {tight}, {leading_zero}) = 0")
            return 0
        res = 0
        upper = s[pos] if tight else 9
        print(f"dp({pos}, {prev1}, {prev2}, {tight}, {leading_zero}) upper={upper}")
        for d in range(0, upper + 1):
            new_tight = tight and (d == upper)
            new_leading_zero = leading_zero and (d == 0)
            if new_leading_zero:
                add = dp(pos + 1, -1, -1, new_tight, new_leading_zero)
                res += add
                print(f"  d={d} new leading zero, add {add}")
            else:
                if prev2 == -1:
                    add = dp(pos + 1, d, prev1, new_tight, new_leading_zero)
                    res += add
                    print(f"  d={d} prev2=-1, add {add}")
                else:
                    add_count = 0
                    if (prev1 > prev2 and prev1 > d) or (prev1 < prev2 and prev1 < d):
                        add_count = 1
                    add = add_count + dp(pos + 1, d, prev1, new_tight, new_leading_zero)
                    res += add
                    print(f"  d={d} prev1={prev1}, prev2={prev2}, add_count={add_count}, total add {add}")
        print(f"dp({pos}, {prev1}, {prev2}, {tight}, {leading_zero}) returns {res}")
        return res
    
    result = dp(0, -1, -1, True, True)
    print(f"count_waviness({x}) = {result}")
    return result

print("count_waviness(4848):", count_waviness(4848))
