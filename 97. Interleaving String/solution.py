from functools import lru_cache

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """
        Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.
        
        An interleaving of two strings s and t is a configuration where s and t are divided into n and m 
        substrings respectively, and the interleaving is s1 + t1 + s2 + t2 + ... or t1 + s1 + t2 + s2 + ...
        
        Approach: Dynamic Programming with memoization
        - Use recursion with memoization to check if we can form s3 by interleaving s1 and s2
        - At each step, we try to match the current character of s3 with either s1 or s2
        - Time: O(m * n), Space: O(m * n) where m = len(s1), n = len(s2)
        """
        if len(s1) + len(s2) != len(s3):
            return False
        
        @lru_cache(maxsize=None)
        def dp(i: int, j: int) -> bool:
            # i = index in s1, j = index in s2
            # k = i + j = index in s3
            k = i + j
            
            # Base case: if we've matched all of s3
            if k == len(s3):
                return True
            
            # Try matching current char of s3 with s1[i]
            if i < len(s1) and s1[i] == s3[k] and dp(i + 1, j):
                return True
            
            # Try matching current char of s3 with s2[j]
            if j < len(s2) and s2[j] == s3[k] and dp(i, j + 1):
                return True
            
            return False
        
        return dp(0, 0)


if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbcbcac"
    print(f"Input: s1 = \"{s1}\", s2 = \"{s2}\", s3 = \"{s3}\"")
    print(f"Output: {sol.isInterleave(s1, s2, s3)}")  # Expected: True
    
    # Example 2
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbbaccc"
    print(f"\nInput: s1 = \"{s1}\", s2 = \"{s2}\", s3 = \"{s3}\"")
    print(f"Output: {sol.isInterleave(s1, s2, s3)}")  # Expected: False
    
    # Example 3
    s1 = ""
    s2 = ""
    s3 = ""
    print(f"\nInput: s1 = \"{s1}\", s2 = \"{s2}\", s3 = \"{s3}\"")
    print(f"Output: {sol.isInterleave(s1, s2, s3)}")  # Expected: True
