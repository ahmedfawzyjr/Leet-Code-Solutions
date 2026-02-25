from typing import List

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        # Simple sorting with a tuple key:
        # First element of the tuple is the number of set bits (1's)
        # Second element is the value itself for tie-breaking
        return sorted(arr, key=lambda x: (bin(x).count('1'), x))
