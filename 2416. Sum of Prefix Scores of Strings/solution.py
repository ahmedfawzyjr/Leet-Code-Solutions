from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.count += 1
            
    def get_score_sum(self, word: str) -> int:
        node = self.root
        score_sum = 0
        for char in word:
            if char not in node.children:
                break
            node = node.children[char]
            score_sum += node.count
        return score_sum

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = Trie()
        for word in words:
            trie.insert(word)
            
        return [trie.get_score_sum(word) for word in words]
