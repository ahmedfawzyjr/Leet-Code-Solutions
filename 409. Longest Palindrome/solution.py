class Solution:
    def longestPalindrome(self, s: str) -> int:
        from collections import Counter
        counts = Counter(s)
        length = 0
        has_odd = False
        
        for count in counts.values():
            if count % 2 == 0:
                length += count
            else:
                length += count - 1
                has_odd = True
        
        return length + 1 if has_odd else length
