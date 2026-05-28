from typing import List

class TrieNode:
    def __init__(self, best_idx: int):
        self.children = {}
        # Stores the index of the string in wordsContainer that has the 
        # smallest length (and earliest index) passing through this node.
        self.best_idx = best_idx

class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        """
        Finds the index of the string in wordsContainer with the longest common suffix for each query.
        Uses a Trie with reversed strings to find the longest common prefix (which is the reversed suffix).
        
        Complexity:
        - Time: O(Sum(len(wordsContainer)) + Sum(len(wordsQuery)))
        - Space: O(Sum(len(wordsContainer)) * AlphabetSize) for the Trie.
        """
        
        # Initial best index (shortest word in wordsContainer, then earliest index)
        # This is for queries that have no common suffix at all.
        global_best_idx = 0
        min_len = len(wordsContainer[0])
        for i in range(1, len(wordsContainer)):
            if len(wordsContainer[i]) < min_len:
                min_len = len(wordsContainer[i])
                global_best_idx = i
        
        root = TrieNode(global_best_idx)
        
        # Build Trie with reversed words from wordsContainer
        for i, word in enumerate(wordsContainer):
            curr = root
            word_len = len(word)
            
            # Helper to check if current word 'i' is better than existing 'best_idx'
            def is_better(new_idx, old_idx):
                if len(wordsContainer[new_idx]) < len(wordsContainer[old_idx]):
                    return True
                if len(wordsContainer[new_idx]) == len(wordsContainer[old_idx]):
                    return new_idx < old_idx
                return False

            # Update root if needed (redundant for root as global_best_idx is already correct, 
            # but good for consistency)
            if is_better(i, root.best_idx):
                root.best_idx = i
                
            for char in reversed(word):
                if char not in curr.children:
                    curr.children[char] = TrieNode(i)
                curr = curr.children[char]
                
                # At each node, store the best index encountered so far
                if is_better(i, curr.best_idx):
                    curr.best_idx = i
        
        # Process queries
        results = []
        for query in wordsQuery:
            curr = root
            best_found = root.best_idx
            
            for char in reversed(query):
                if char in curr.children:
                    curr = curr.children[char]
                    best_found = curr.best_idx
                else:
                    break
            results.append(best_found)
            
        return results
