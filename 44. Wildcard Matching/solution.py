class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        Implement wildcard pattern matching with support for '?' and '*'.
        
        '?' - Matches any single character
        '*' - Matches any sequence of characters (including empty sequence)
        
        Dynamic Programming approach:
        dp[i][j] = True if s[0:i] matches p[0:j]
        
        Time Complexity: O(m * n) where m = len(s), n = len(p)
        Space Complexity: O(m * n), can be optimized to O(n)
        """
        m, n = len(s), len(p)
        
        # dp[i][j] = True if s[0:i] matches p[0:j]
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        
        # Empty pattern matches empty string
        dp[0][0] = True
        
        # Handle patterns like '*', '**', '***' that can match empty string
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 1]
        
        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    # '*' matches empty sequence OR one more character
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
                elif p[j - 1] == '?' or p[j - 1] == s[i - 1]:
                    # '?' matches any single character
                    # Or exact character match
                    dp[i][j] = dp[i - 1][j - 1]
        
        return dp[m][n]
    
    def isMatch_optimized(self, s: str, p: str) -> bool:
        """
        Space-optimized two-pointer approach with backtracking.
        
        Time Complexity: O(m * n) worst case, O(m + n) average
        Space Complexity: O(1)
        """
        m, n = len(s), len(p)
        s_idx, p_idx = 0, 0
        star_idx = -1  # Position of last '*' in pattern
        s_tmp_idx = -1  # Position in s when we matched '*'
        
        while s_idx < m:
            # Exact match or '?' match
            if p_idx < n and (p[p_idx] == '?' or p[p_idx] == s[s_idx]):
                s_idx += 1
                p_idx += 1
            # '*' found - record position and try matching empty sequence first
            elif p_idx < n and p[p_idx] == '*':
                star_idx = p_idx
                s_tmp_idx = s_idx
                p_idx += 1
            # Mismatch - backtrack to last '*' and try matching one more character
            elif star_idx != -1:
                p_idx = star_idx + 1
                s_tmp_idx += 1
                s_idx = s_tmp_idx
            # No match and no '*' to backtrack to
            else:
                return False
        
        # Check remaining pattern characters (must all be '*')
        while p_idx < n and p[p_idx] == '*':
            p_idx += 1
        
        return p_idx == n


# Test cases
if __name__ == "__main__":
    sol = Solution()
    
    # Example 1: s = "aa", p = "a" -> Output: false
    print(sol.isMatch("aa", "a"))  # False
    
    # Example 2: s = "aa", p = "*" -> Output: true
    print(sol.isMatch("aa", "*"))  # True
    
    # Example 3: s = "cb", p = "?a" -> Output: false
    print(sol.isMatch("cb", "?a"))  # False
    
    # Additional tests
    print(sol.isMatch("adceb", "*a*b"))  # True
    print(sol.isMatch("acdcb", "a*c?b"))  # False
