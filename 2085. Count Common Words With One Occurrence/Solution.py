from collections import Counter
from typing import List


class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        """
        Counts the number of strings that appear exactly once in each of the two arrays.

        Approach:
        1. Count frequency of words in `words1` using `Counter`.
        2. Count frequency of words in `words2` using `Counter`.
        3. Iterate through `words1` (or its keys) and count how many words have 
           frequency 1 in `count1` AND frequency 1 in `count2`.

        Complexity:
        - Time Complexity: O(N + M), where N = len(words1) and M = len(words2).
        - Space Complexity: O(N + M) to store word frequencies.
        """
        count1 = Counter(words1)
        count2 = Counter(words2)
        
        ans = 0
        for word, cnt1 in count1.items():
            if cnt1 == 1 and count2[word] == 1:
                ans += 1
                
        return ans


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    # Input: words1 = ["leetcode","is","amazing","as","is"], words2 = ["amazing","leetcode","is"]
    # Output: 2
    res1 = sol.countWords(["leetcode", "is", "amazing", "as", "is"], ["amazing", "leetcode", "is"])
    assert res1 == 2, f"Failed Example 1: got {res1}"

    # Example 2
    # Input: words1 = ["b","bb","bbb"], words2 = ["a","aa","aaa"]
    # Output: 0
    res2 = sol.countWords(["b", "bb", "bbb"], ["a", "aa", "aaa"])
    assert res2 == 0, f"Failed Example 2: got {res2}"

    # Example 3
    # Input: words1 = ["a","ab"], words2 = ["a","a","a","ab"]
    # Output: 1
    res3 = sol.countWords(["a", "ab"], ["a", "a", "a", "ab"])
    assert res3 == 1, f"Failed Example 3: got {res3}"

    print("All test cases passed successfully!")
