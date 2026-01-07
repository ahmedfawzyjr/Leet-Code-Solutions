class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        memo = {}

        def solve(s1, s2):
            if (s1, s2) in memo:
                return memo[(s1, s2)]
            
            if s1 == s2:
                return True
            
            if sorted(s1) != sorted(s2):
                return False
            
            n = len(s1)
            for i in range(1, n):
                # Case 1: No swap
                if solve(s1[:i], s2[:i]) and solve(s1[i:], s2[i:]):
                    memo[(s1, s2)] = True
                    return True
                # Case 2: Swap
                if solve(s1[:i], s2[n-i:]) and solve(s1[i:], s2[:n-i]):
                    memo[(s1, s2)] = True
                    return True
            
            memo[(s1, s2)] = False
            return False

        return solve(s1, s2)

if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    s1_1 = "great"
    s2_1 = "rgeat"
    print(f"Input: s1 = \"{s1_1}\", s2 = \"{s2_1}\"")
    print(f"Output: {sol.isScramble(s1_1, s2_1)}")
    
    # Example 2
    s1_2 = "abcde"
    s2_2 = "caebd"
    print(f"Input: s1 = \"{s1_2}\", s2 = \"{s2_2}\"")
    print(f"Output: {sol.isScramble(s1_2, s2_2)}")
    
    # Example 3
    s1_3 = "a"
    s2_3 = "a"
    print(f"Input: s1 = \"{s1_3}\", s2 = \"{s2_3}\"")
    print(f"Output: {sol.isScramble(s1_3, s2_3)}")
