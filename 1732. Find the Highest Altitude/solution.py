
from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        current = 0
        max_alt = 0
        for g in gain:
            current += g
            if current > max_alt:
                max_alt = current
        return max_alt
