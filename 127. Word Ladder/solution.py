from typing import List
from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        
        queue = deque([(beginWord, 1)])
        visited = {beginWord}
        
        while queue:
            current_word, level = queue.popleft()
            
            if current_word == endWord:
                return level
            
            for i in range(len(current_word)):
                prefix = current_word[:i]
                suffix = current_word[i+1:]
                for char in 'abcdefghijklmnopqrstuvwxyz':
                    neighbor = prefix + char + suffix
                    if neighbor in wordSet and neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, level + 1))
                        
        return 0

if __name__ == "__main__":
    solution = Solution()
    
    # Example 1
    beginWord1 = "hit"
    endWord1 = "cog"
    wordList1 = ["hot","dot","dog","lot","log","cog"]
    output1 = solution.ladderLength(beginWord1, endWord1, wordList1)
    print(f"Example 1: Output: {output1}")
    assert output1 == 5
    
    # Example 2
    beginWord2 = "hit"
    endWord2 = "cog"
    wordList2 = ["hot","dot","dog","lot","log"]
    output2 = solution.ladderLength(beginWord2, endWord2, wordList2)
    print(f"Example 2: Output: {output2}")
    assert output2 == 0

    print("All test cases passed!")
