class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        """
        Determines whether the given sentence is a pangram (contains all 26 English letters).

        Approach:
        1. Fast path: If the length of `sentence` is less than 26, it cannot possibly contain
           all 26 distinct letters of the English alphabet, so return False immediately.
        2. Set of unique characters: Convert the lowercase English string into a set of distinct
           characters.
        3. Check if the number of unique characters equals 26.

        Complexity:
        - Time Complexity: O(n), where n is the length of `sentence`.
        - Space Complexity: O(1) auxiliary space (or O(Σ) where Σ = 26 is the alphabet size).
        """
        if len(sentence) < 26:
            return False
        return len(set(sentence)) == 26


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    # Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
    # Output: True
    s1 = "thequickbrownfoxjumpsoverthelazydog"
    assert sol.checkIfPangram(s1) is True, f"Failed Example 1: got {sol.checkIfPangram(s1)}"

    # Example 2
    # Input: sentence = "leetcode"
    # Output: False
    s2 = "leetcode"
    assert sol.checkIfPangram(s2) is False, f"Failed Example 2: got {sol.checkIfPangram(s2)}"

    # Edge cases
    # Length < 26 (25 chars)
    assert sol.checkIfPangram("abcdefghijklmnopqrstuvwxy") is False
    # Exactly 26 distinct letters in alphabetical order
    assert sol.checkIfPangram("abcdefghijklmnopqrstuvwxyz") is True
    # With duplicate letters covering all 26
    assert sol.checkIfPangram("abcdefghijklmnopqrstuvwxyzaabbcc") is True
    # 1000 characters missing one letter
    assert sol.checkIfPangram("a" * 999 + "b") is False

    print("All test cases passed successfully!")
