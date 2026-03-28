class Solution:
    def findTheString(self, lcp: list[list[int]]) -> str:
        n = len(lcp)
        s = [""] * n
        next_char_idx = 0
        
        # Greedy construction
        for i in range(n):
            if s[i]:
                continue
            if next_char_idx >= 26:
                return ""
            char = chr(ord('a') + next_char_idx)
            next_char_idx += 1
            for j in range(i, n):
                if lcp[i][j] > 0:
                    s[j] = char
        
        # Validate all characters assigned
        for char_val in s:
            if not char_val:
                return ""
        
        res = "".join(s)
        
        # Verification using DP
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            char_i = res[i]
            for j in range(n - 1, -1, -1):
                char_j = res[j]
                if char_i == char_j:
                    dp[i][j] = dp[i + 1][j + 1] + 1
                else:
                    dp[i][j] = 0
                
                if dp[i][j] != lcp[i][j]:
                    return ""
        
        return res
