import math

class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        if x + y < target:
            return False
        
        if x == 0 or y == 0:
            return target == 0 or x + y == target
            
        return target % math.gcd(x, y) == 0
