
from functools import lru_cache

def count_waviness_dp_debug(x, target):
    if x < 100:
        return 0
    s = list(map(int, str(x)))
    n = len(s)
    target_digits = list(map(int, str(target)))
    print("Target digits:", target_digits)
    
    @lru_cache(maxsize=None)
    def dp(pos, prev1, prev2, tight, leading_zero, path_tuple):
        path = list(path_tuple)
        if pos == n:
            if path == target_digits:
                print(f"Reached target! path={path}")
            return 0
        res = 0
        upper = s[pos] if tight else 9
        for d in range(0, upper + 1):
            new_tight = tight and (d == upper)
            new_leading_zero = leading_zero and (d == 0)
            new_path = path + [d] if not new_leading_zero else path
            new_path_tuple = tuple(new_path)
            if new_leading_zero:
                add = dp(pos + 1, -1, -1, new_tight, new_leading_zero, new_path_tuple)
                res += add
            else:
                if prev2 == -1:
                    add = dp(pos + 1, d, prev1, new_tight, new_leading_zero, new_path_tuple)
                    res += add
                else:
                    add_count = 0
                    if (prev1 > prev2 and prev1 > d) or (prev1 < prev2 and prev1 < d):
                        add_count = 1
                    if new_path[:len(target_digits)] == target_digits[:pos+1]:
                        print(f"pos={pos}, path={new_path}, prev1={prev1}, prev2={prev2}, d={d}, add_count={add_count}")
                    add = add_count + dp(pos + 1, d, prev1, new_tight, new_leading_zero, new_path_tuple)
                    res += add
        return res
    
    result = dp(0, -1, -1, True, True, tuple([]))
    print("result:", result)
    return result

count_waviness_dp_debug(1011, 1011)
