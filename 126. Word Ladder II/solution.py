from typing import List
from collections import defaultdict, deque

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []
        
        # BFS to build the graph (parents map)
        layer = {beginWord}
        parents = defaultdict(list)
        
        while layer:
            # Remove words in the current layer from the wordSet to prevent cycles
            # and ensure we only move forward in the shortest path.
            # We remove them *after* processing the whole layer because multiple words
            # in the current layer might lead to the same word in the next layer.
            wordSet -= layer
            next_layer = set()
            
            for word in layer:
                for i in range(len(word)):
                    prefix = word[:i]
                    suffix = word[i+1:]
                    for char in 'abcdefghijklmnopqrstuvwxyz':
                        neighbor = prefix + char + suffix
                        if neighbor in wordSet:
                            next_layer.add(neighbor)
                            parents[neighbor].append(word)
            
            if endWord in next_layer:
                break
            
            layer = next_layer
        
        # DFS/Backtracking to reconstruct paths
        res = []
        def backtrack(word, path):
            if word == beginWord:
                res.append(path[::-1])
                return
            
            for parent in parents[word]:
                backtrack(parent, path + [parent])
                
        if endWord in parents:
            backtrack(endWord, [endWord])
            
        return res

if __name__ == "__main__":
    solution = Solution()
    
    # Example 1
    beginWord1 = "hit"
    endWord1 = "cog"
    wordList1 = ["hot","dot","dog","lot","log","cog"]
    output1 = solution.findLadders(beginWord1, endWord1, wordList1)
    print(f"Example 1: Output: {output1}")
    expected1 = [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
    # Sort to compare as order doesn't matter
    output1_sorted = sorted([sorted(path) for path in output1])
    expected1_sorted = sorted([sorted(path) for path in expected1])
    # Note: The problem asks for sequences, so order within path matters. 
    # But the order of paths in the result list doesn't matter.
    # Let's just check if the lengths are correct and valid paths exist.
    assert len(output1) == 2
    assert ["hit","hot","dot","dog","cog"] in output1
    assert ["hit","hot","lot","log","cog"] in output1
    
    # Example 2
    beginWord2 = "hit"
    endWord2 = "cog"
    wordList2 = ["hot","dot","dog","lot","log"]
    output2 = solution.findLadders(beginWord2, endWord2, wordList2)
    print(f"Example 2: Output: {output2}")
    assert output2 == []

    print("All test cases passed!")
