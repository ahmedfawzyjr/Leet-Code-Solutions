class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        reversed_x = 0
        while x != 0:
            pop = x % 10
            x //= 10
            
            if reversed_x > (INT_MAX - pop) // 10:
                return 0
            
            reversed_x = reversed_x * 10 + pop
        
        return sign * reversed_x
