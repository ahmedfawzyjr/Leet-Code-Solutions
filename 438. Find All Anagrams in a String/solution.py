from typing import List
from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_len, p_len = len(s), len(p)
        if s_len < p_len:
            return []
        
        p_count = Counter(p)
        s_count = Counter(s[:p_len-1])
        
        res = []
        for i in range(p_len - 1, s_len):
            # Add character at i to window
            s_count[s[i]] += 1
            
            # Start index of current window
            start_idx = i - p_len + 1
            
            # Check if current window matches p_count
            if s_count == p_count:
                res.append(start_idx)
            
            # Remove character at start_idx from window for next iteration
            s_count[s[start_idx]] -= 1
            if s_count[s[start_idx]] == 0:
                del s_count[s[start_idx]]
                
        return res
