from functools import lru_cache

class Solution:
    def numDecodings(self, s: str) -> int:
        """
        Given a string s containing only digits, return the number of ways to decode it.
        
        A message containing letters from A-Z can be encoded into numbers using:
        'A' -> "1", 'B' -> "2", ..., 'Z' -> "26"
        
        Approach: Dynamic Programming
        - dp[i] = number of ways to decode s[i:]
        - At each position, we can take 1 digit (if valid) or 2 digits (if valid)
        - Time: O(n), Space: O(1) with optimization
        """
        if not s or s[0] == '0':
            return 0
        
        n = len(s)
        
        @lru_cache(maxsize=None)
        def dp(i: int) -> int:
            # Base case: reached the end
            if i == n:
                return 1
            
            # Leading zero is invalid
            if s[i] == '0':
                return 0
            
            # Take one digit
            ways = dp(i + 1)
            
            # Take two digits if valid (10-26)
            if i + 1 < n:
                two_digit = int(s[i:i+2])
                if 10 <= two_digit <= 26:
                    ways += dp(i + 2)
            
            return ways
        
        return dp(0)


if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    s1 = "12"
    print(f"Input: s = \"{s1}\"")
    print(f"Output: {sol.numDecodings(s1)}")  # Expected: 2
    
    # Example 2
    s2 = "226"
    print(f"\nInput: s = \"{s2}\"")
    print(f"Output: {sol.numDecodings(s2)}")  # Expected: 3
    
    # Example 3
    s3 = "06"
    print(f"\nInput: s = \"{s3}\"")
    print(f"Output: {sol.numDecodings(s3)}")  # Expected: 0
