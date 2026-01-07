class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        """
        DFS/Backtracking approach to find if word exists in the grid.
        
        Time: O(m * n * 4^L) where L = len(word), m*n = grid size
        Space: O(L) for recursion stack
        """
        if not board or not board[0]:
            return False
        
        rows, cols = len(board), len(board[0])
        
        def dfs(row: int, col: int, index: int) -> bool:
            # Base case: all characters matched
            if index == len(word):
                return True
            
            # Boundary check and character match
            if (row < 0 or row >= rows or 
                col < 0 or col >= cols or 
                board[row][col] != word[index]):
                return False
            
            # Mark current cell as visited by temporarily changing it
            temp = board[row][col]
            board[row][col] = '#'  # Mark as visited
            
            # Explore all 4 directions
            found = (dfs(row + 1, col, index + 1) or  # Down
                     dfs(row - 1, col, index + 1) or  # Up
                     dfs(row, col + 1, index + 1) or  # Right
                     dfs(row, col - 1, index + 1))    # Left
            
            # Restore the cell (backtrack)
            board[row][col] = temp
            
            return found
        
        # Try starting from each cell
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:  # Optimization: only start if first char matches
                    if dfs(i, j, 0):
                        return True
        
        return False


# Test cases
if __name__ == "__main__":
    sol = Solution()
    
    # Test case 1
    board1 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    print(f"Test 1: {sol.exist(board1, 'ABCCED')}")  # Expected: True
    
    # Test case 2
    board2 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    print(f"Test 2: {sol.exist(board2, 'SEE')}")  # Expected: True
    
    # Test case 3
    board3 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    print(f"Test 3: {sol.exist(board3, 'ABCB')}")  # Expected: False
