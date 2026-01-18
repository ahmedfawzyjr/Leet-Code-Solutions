from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Build Trie
        root = TrieNode()
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.word = word
            
        rows, cols = len(board), len(board[0])
        result = set()
        
        def backtrack(r, c, node):
            char = board[r][c]
            if char not in node.children:
                return
            
            next_node = node.children[char]
            if next_node.word:
                result.add(next_node.word)
                # Optimization: remove word from Trie to avoid duplicates and speed up
                # However, for simplicity and correctness in all cases (like prefix words), we might keep it or handle carefully.
                # For this problem, simply adding to set is enough.
            
            board[r][c] = '#' # Mark as visited
            
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != '#':
                    backtrack(nr, nc, next_node)
            
            board[r][c] = char # Backtrack
            
            # Optimization: prune leaf nodes
            if not next_node.children:
                del node.children[char]

        for r in range(rows):
            for c in range(cols):
                backtrack(r, c, root)
                
        return list(result)

if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
    words = ["oath","pea","eat","rain"]
    # Expected: ["eat","oath"] (order doesn't matter)
    print(f"Example 1: {sorted(sol.findWords(board, words))}") 
    
    # Example 2
    board = [["a","b"],["c","d"]]
    words = ["abcb"]
    # Expected: []
    print(f"Example 2: {sol.findWords(board, words)}")
