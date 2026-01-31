from collections import Counter

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        n = len(s)
        if n < k:
            return 0
            
        counts = Counter(s)
        for char, count in counts.items():
            if count < k:
                return max(self.longestSubstring(sub, k) for sub in s.split(char))
                
        return n
