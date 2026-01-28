from typing import List

class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        MOD = 1337
        
        def power(base, exp):
            res = 1
            base %= MOD
            while exp > 0:
                if exp % 2 == 1:
                    res = (res * base) % MOD
                base = (base * base) % MOD
                exp //= 2
            return res
            
        if not b:
            return 1
            
        last_digit = b.pop()
        part1 = power(a, last_digit)
        part2 = power(self.superPow(a, b), 10)
        
        return (part1 * part2) % MOD
