from collections import Counter
from typing import List


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        """
        Finds all characters (including duplicates) that appear in every string in words.

        Approach:
        1. Initialize a frequency counter with the character counts of the first word.
        2. For each remaining word in `words`, compute its character counts and take
           the multiset intersection (&) with our running counter, which keeps the
           minimum count of each character seen so far across all words.
        3. Expand the resulting character frequencies into a list using Counter.elements().

        Complexity:
        - Time Complexity: O(N * L), where N is the number of words and L is the maximum length of a word.
        - Space Complexity: O(1) auxiliary space (or O(Σ) where Σ = 26 is the alphabet size).
        """
        common = Counter(words[0])
        for word in words[1:]:
            common &= Counter(word)
        return list(common.elements())


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    # Input: words = ["bella","label","roller"]
    # Output: ["e","l","l"]
    res1 = sorted(sol.commonChars(["bella", "label", "roller"]))
    assert res1 == ["e", "l", "l"], f"Failed Example 1: got {res1}"

    # Example 2
    # Input: words = ["cool","lock","cook"]
    # Output: ["c","o"]
    res2 = sorted(sol.commonChars(["cool", "lock", "cook"]))
    assert res2 == ["c", "o"], f"Failed Example 2: got {res2}"

    # Additional Test Cases:
    # Single word
    res3 = sorted(sol.commonChars(["hello"]))
    assert res3 == ["e", "h", "l", "l", "o"], f"Failed single word: got {res3}"

    # No common characters
    res4 = sol.commonChars(["abc", "def", "ghi"])
    assert res4 == [], f"Failed no common characters: got {res4}"

    # Identical words with duplicates
    res5 = sorted(sol.commonChars(["aabbcc", "aabbcc"]))
    assert res5 == ["a", "a", "b", "b", "c", "c"], f"Failed identical words: got {res5}"

    # Varying counts
    res6 = sorted(sol.commonChars(["bbbaaa", "aabbb", "baaab"]))
    assert res6 == ["a", "a", "b", "b"], f"Failed varying counts: got {res6}"

    print("All test cases passed successfully!")
