class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        s = s + s  # To handle Type-1: Remove and append to end
        
        # Two target alternating strings:
        # target1: 010101...
        # target2: 101010...
        target1 = ""
        target2 = ""
        for i in range(len(s)):
            target1 += "0" if i % 2 == 0 else "1"
            target2 += "1" if i % 2 == 0 else "0"
            
        res = len(s)
        diff1, diff2 = 0, 0
        
        # Sliding window of size n
        for i in range(len(s)):
            if s[i] != target1[i]:
                diff1 += 1
            if s[i] != target2[i]:
                diff2 += 1
            
            if i >= n:  # Pop left character from window
                if s[i - n] != target1[i - n]:
                    diff1 -= 1
                if s[i - n] != target2[i - n]:
                    diff2 -= 1
            
            if i >= n - 1:
                res = min(res, diff1, diff2)
                
        return res
