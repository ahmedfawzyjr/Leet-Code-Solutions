from typing import List

class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        k = len(arr) // 20
        trimmed = arr[k:-k]
        return sum(trimmed) / len(trimmed)
