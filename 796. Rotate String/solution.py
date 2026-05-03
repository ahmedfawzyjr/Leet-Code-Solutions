class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        """
        Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.
        A shift on s consists of moving the leftmost character of s to the rightmost position.
        
        Complexity:
        - Time: O(N), where N is the length of string s. String concatenation s + s takes O(N), and substring search takes O(N).
        - Space: O(N) to store the concatenated string s + s.
        """
        return len(s) == len(goal) and goal in (s + s)

# Test cases
if __name__ == "__main__":
    sol = Solution()
    print(sol.rotateString("abcde", "cdeab"))  # Expected: True
    print(sol.rotateString("abcde", "abced"))  # Expected: False
