from typing import List

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        word_to_idx = {w: i for i, w in enumerate(words)}
        res = []
        
        for i, word in enumerate(words):
            n = len(word)
            for j in range(n + 1):
                prefix = word[:j]
                suffix = word[j:]
                
                # Case 1: Prefix is palindrome, check if reversed suffix exists
                if prefix == prefix[::-1]:
                    rev_suffix = suffix[::-1]
                    if rev_suffix in word_to_idx and word_to_idx[rev_suffix] != i:
                        res.append([word_to_idx[rev_suffix], i])
                
                # Case 2: Suffix is palindrome, check if reversed prefix exists
                # j < n to avoid duplicate cases already handled in Case 1
                if j < n and suffix == suffix[::-1]:
                    rev_prefix = prefix[::-1]
                    if rev_prefix in word_to_idx and word_to_idx[rev_prefix] != i:
                        res.append([i, word_to_idx[rev_prefix]])
                        
        return res

if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    words1 = ["abcd","dcba","lls","s","sssll"]
    print(f"Example 1: {sol.palindromePairs(words1)}") # Expected: [[0,1],[1,0],[3,2],[2,4]]
    
    # Example 2
    words2 = ["bat","tab","cat"]
    print(f"Example 2: {sol.palindromePairs(words2)}") # Expected: [[0,1],[1,0]]
    
    # Example 3
    words3 = ["a",""]
    print(f"Example 3: {sol.palindromePairs(words3)}") # Expected: [[0,1],[1,0]]
