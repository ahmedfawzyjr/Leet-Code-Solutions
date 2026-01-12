class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        
        # is_palindrome[i][j] will be True if s[i:j+1] is a palindrome
        is_palindrome = [[False] * n for _ in range(n)]
        
        # dp[i] will store the minimum cuts needed for s[:i+1]
        dp = [0] * n
        
        for i in range(n):
            min_cuts = i  # Max cuts needed is i (cut at every character)
            for j in range(i + 1):
                # Check if s[j:i+1] is a palindrome
                if s[j] == s[i] and (i - j < 2 or is_palindrome[j + 1][i - 1]):
                    is_palindrome[j][i] = True
                    if j == 0:
                        min_cuts = 0
                    else:
                        min_cuts = min(min_cuts, dp[j - 1] + 1)
            dp[i] = min_cuts
            
        return dp[n - 1]

if __name__ == "__main__":
    solution = Solution()
    
    # Example 1
    s1 = "aab"
    assert solution.minCut(s1) == 1, f"Test case 1 failed: {solution.minCut(s1)}"
    print("Test case 1 passed")
    
    # Example 2
    s2 = "a"
    assert solution.minCut(s2) == 0, f"Test case 2 failed: {solution.minCut(s2)}"
    print("Test case 2 passed")
    
    # Example 3
    s3 = "ab"
    assert solution.minCut(s3) == 1, f"Test case 3 failed: {solution.minCut(s3)}"
    print("Test case 3 passed")
