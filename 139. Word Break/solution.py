from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True
        
        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
                    
        return dp[len(s)]

if __name__ == "__main__":
    solution = Solution()
    
    # Example 1
    s1 = "leetcode"
    wordDict1 = ["leet", "code"]
    assert solution.wordBreak(s1, wordDict1) == True, f"Test case 1 failed: {solution.wordBreak(s1, wordDict1)}"
    print("Test case 1 passed")
    
    # Example 2
    s2 = "applepenapple"
    wordDict2 = ["apple", "pen"]
    assert solution.wordBreak(s2, wordDict2) == True, f"Test case 2 failed: {solution.wordBreak(s2, wordDict2)}"
    print("Test case 2 passed")
    
    # Example 3
    s3 = "catsandog"
    wordDict3 = ["cats", "dog", "sand", "and", "cat"]
    assert solution.wordBreak(s3, wordDict3) == False, f"Test case 3 failed: {solution.wordBreak(s3, wordDict3)}"
    print("Test case 3 passed")
