from collections import Counter

class Solution:
    def minimumPushes(self, word: str) -> int:
        counts = Counter(word)
        sorted_freqs = sorted(counts.values(), reverse=True)
        
        ans = 0
        for i, freq in enumerate(sorted_freqs):
            ans += (i // 8 + 1) * freq
            
        return ans
