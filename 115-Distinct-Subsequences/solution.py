class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        
        # dp[i][j] will store the number of distinct subsequences of s[i:] equal to t[j:]
        # We can optimize space to O(n) since we only need the previous row (or effectively just current row updates)
        # But let's stick to a clear 2D DP first for clarity or 1D if simple enough.
        # Let's use 1D array dp where dp[j] means number of distinct subsequences of s[:i] equal to t[:j]
        
        # Initialize dp array
        # dp[j] corresponds to t[:j]
        # We need to handle the empty string case for t, which is always 1 match (delete all chars from s)
        
        dp = [0] * (n + 1)
        dp[0] = 1
        
        for i in range(1, m + 1):
            # We must iterate backwards to avoid using results from the current character of s for the same character of s
            # effectively simulating using the 'previous row' in the 2D matrix
            for j in range(n, 0, -1):
                if s[i-1] == t[j-1]:
                    dp[j] += dp[j-1]
                    
        return dp[n]

if __name__ == "__main__":
    solution = Solution()
    
    # Example 1
    s1 = "rabbbit"
    t1 = "rabbit"
    result1 = solution.numDistinct(s1, t1)
    print(f"Test Case 1: Expected 3, Got {result1}")
    assert result1 == 3
    
    # Example 2
    s2 = "babgbag"
    t2 = "bag"
    result2 = solution.numDistinct(s2, t2)
    print(f"Test Case 2: Expected 5, Got {result2}")
    assert result2 == 5
    
    print("All test cases passed!")
