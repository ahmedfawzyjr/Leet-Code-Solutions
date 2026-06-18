
from functools import lru_cache

class Solution:
    def leastOpsExpressTarget(self, x: int, target: int) -> int:
        @lru_cache(maxsize=None)
        def dfs(num):
            if num == 0:
                return 0
            if num < x:
                # Either take num * (x/x) which is 2*num ops, or (x - num)*(x/x) which is 2*(x - num) ops
                return min(2 * num, 2 * (x - num))
            
            power = 0
            while x ** (power + 1) <= num:
                power += 1
            val = x ** power
            # Option 1: take the current power
            res1 = power + dfs(num - val)
            # Option 2: take (x - (num % val)), which is equivalent to adding val * x and subtracting (x * val - num)
            res2 = (power + 1) + dfs(val * x - num)
            return min(res1, res2)
        
        return dfs(target) - 1
