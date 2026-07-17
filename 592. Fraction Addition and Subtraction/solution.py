import math
import re

class Solution:
    def fractionAddition(self, expression: str) -> str:
        # Find all fractions in format [+-]num/den
        fractions = re.findall(r'[+-]?\d+/\d+', expression)
        
        num, den = 0, 1
        for frac in fractions:
            f_num, f_den = map(int, frac.split('/'))
            # Add: num/den + f_num/f_den = (num * f_den + den * f_num) / (den * f_den)
            num = num * f_den + den * f_num
            den = den * f_den
            
            # Simplify
            common = math.gcd(abs(num), den)
            num //= common
            den //= common
            
        return f"{num}/{den}"
