class Solution:
    def longestValidParentheses(self, s: str) -> int:
        """
        Find the length of the longest valid (well-formed) parentheses substring.
        
        Uses a stack-based approach where the stack stores indices.
        We push -1 initially as a base for valid substring calculation.
        
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        max_length = 0
        stack = [-1]  # Base index for calculating valid length
        
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            else:  # char == ')'
                stack.pop()
                
                if not stack:
                    # No matching '(', push current index as new base
                    stack.append(i)
                else:
                    # Valid parentheses found, calculate length
                    max_length = max(max_length, i - stack[-1])
        
        return max_length
    
    def longestValidParentheses_dp(self, s: str) -> int:
        """
        Alternative solution using Dynamic Programming.
        
        dp[i] = length of longest valid parentheses ending at index i
        
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        if not s:
            return 0
        
        n = len(s)
        dp = [0] * n
        max_length = 0
        
        for i in range(1, n):
            if s[i] == ')':
                if s[i - 1] == '(':
                    # Case: ...()
                    dp[i] = (dp[i - 2] if i >= 2 else 0) + 2
                elif i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == '(':
                    # Case: ...))
                    dp[i] = dp[i - 1] + 2 + (dp[i - dp[i - 1] - 2] if i - dp[i - 1] - 2 >= 0 else 0)
                
                max_length = max(max_length, dp[i])
        
        return max_length
