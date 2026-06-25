class Solution:
    def findGoodStrings(self, n: int, s1: str, s2: str, evil: str) -> int:
        MOD = 10**9 + 7
        evil_len = len(evil)
        
        # Precompute KMP failure/prefix function
        pi = [0] * evil_len
        j = 0
        for i in range(1, evil_len):
            while j > 0 and evil[i] != evil[j]:
                j = pi[j - 1]
            if evil[i] == evil[j]:
                j += 1
            pi[i] = j
            
        def count(s: str) -> int:
            memo = {}
            
            def dfs(idx: int, evil_matched: int, is_tight: bool) -> int:
                if evil_matched == evil_len:
                    return 0
                if idx == n:
                    return 1
                
                state = (idx, evil_matched, is_tight)
                if state in memo:
                    return memo[state]
                
                limit_char = s[idx] if is_tight else 'z'
                ans = 0
                for ord_c in range(ord('a'), ord(limit_char) + 1):
                    c = chr(ord_c)
                    next_tight = is_tight and (c == limit_char)
                    
                    next_evil = evil_matched
                    while next_evil > 0 and evil[next_evil] != c:
                        next_evil = pi[next_evil - 1]
                    if evil[next_evil] == c:
                        next_evil += 1
                        
                    ans = (ans + dfs(idx + 1, next_evil, next_tight)) % MOD
                    
                memo[state] = ans
                return ans
            
            return dfs(0, 0, True)
            
        ans = (count(s2) - count(s1) + (1 if evil not in s1 else 0)) % MOD
        return ans
