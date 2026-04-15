from typing import List

class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        res = n
        found = False
        for i, word in enumerate(words):
            if word == target:
                found = True
                dist = abs(i - startIndex)
                res = min(res, dist, n - dist)
        
        return res if found else -1
