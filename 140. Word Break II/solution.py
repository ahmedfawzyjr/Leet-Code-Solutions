from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)
        memo = {}

        def backtrack(start_index):
            if start_index == len(s):
                return [""]
            
            if start_index in memo:
                return memo[start_index]
            
            sentences = []
            for end_index in range(start_index + 1, len(s) + 1):
                word = s[start_index:end_index]
                if word in word_set:
                    sub_sentences = backtrack(end_index)
                    for sub in sub_sentences:
                        if sub:
                            sentences.append(word + " " + sub)
                        else:
                            sentences.append(word)
            
            memo[start_index] = sentences
            return sentences

        return backtrack(0)

if __name__ == "__main__":
    solution = Solution()
    
    # Example 1
    s1 = "catsanddog"
    wordDict1 = ["cat", "cats", "and", "sand", "dog"]
    expected1 = ["cats and dog", "cat sand dog"]
    result1 = solution.wordBreak(s1, wordDict1)
    assert sorted(result1) == sorted(expected1), f"Test case 1 failed: {result1}"
    print("Test case 1 passed")
    
    # Example 2
    s2 = "pineapplepenapple"
    wordDict2 = ["apple", "pen", "applepen", "pine", "pineapple"]
    expected2 = ["pine apple pen apple", "pineapple pen apple", "pine applepen apple"]
    result2 = solution.wordBreak(s2, wordDict2)
    assert sorted(result2) == sorted(expected2), f"Test case 2 failed: {result2}"
    print("Test case 2 passed")
    
    # Example 3
    s3 = "catsandog"
    wordDict3 = ["cats", "dog", "sand", "and", "cat"]
    expected3 = []
    result3 = solution.wordBreak(s3, wordDict3)
    assert sorted(result3) == sorted(expected3), f"Test case 3 failed: {result3}"
    print("Test case 3 passed")
