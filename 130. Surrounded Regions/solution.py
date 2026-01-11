from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        
        m, n = len(board), len(board[0])
        
        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n or board[r][c] != 'O':
                return
            board[r][c] = 'T'
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
            
        # 1. Mark 'O's on the border and their connected 'O's as 'T' (temporary)
        for i in range(m):
            dfs(i, 0)
            dfs(i, n-1)
            
        for j in range(n):
            dfs(0, j)
            dfs(m-1, j)
            
        # 2. Iterate through the board:
        #    - Change remaining 'O's to 'X' (captured)
        #    - Change 'T's back to 'O' (safe)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'T':
                    board[i][j] = 'O'

if __name__ == "__main__":
    solution = Solution()
    
    # Example 1
    board1 = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
    solution.solve(board1)
    print(f"Example 1: Output: {board1}")
    expected1 = [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
    assert board1 == expected1
    
    # Example 2
    board2 = [["X"]]
    solution.solve(board2)
    print(f"Example 2: Output: {board2}")
    expected2 = [["X"]]
    assert board2 == expected2

    print("All test cases passed!")
