class Solution:
    def findSubstringInWraparoundString(self, s: str) -> int:
        if not s:
            return 0
        
        # count[i] stores the max length of contiguous substring ending with character i
        count = [0] * 26
        current_len = 0
        
        for i in range(len(s)):
            # Check if current character is consecutive to the previous one
            if i > 0 and (ord(s[i]) - ord(s[i-1]) == 1 or ord(s[i-1]) - ord(s[i]) == 25):
                current_len += 1
            else:
                current_len = 1
            
            idx = ord(s[i]) - ord('a')
            count[idx] = max(count[idx], current_len)
            
        return sum(count)
