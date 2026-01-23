from typing import List

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        
        State transitions:
        0 -> 0: 0
        1 -> 1: 1
        1 -> 0: 2 (was live, now dead)
        0 -> 1: 3 (was dead, now live)
        """
        rows = len(board)
        cols = len(board[0])
        
        neighbors = [(1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1)]
        
        for r in range(rows):
            for c in range(cols):
                live_neighbors = 0
                for dr, dc in neighbors:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and (board[nr][nc] == 1 or board[nr][nc] == 2):
                        live_neighbors += 1
                
                # Rule 1 or 3
                if board[r][c] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[r][c] = 2
                # Rule 4
                if board[r][c] == 0 and live_neighbors == 3:
                    board[r][c] = 3
        
        # Second pass to finalize states
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 2:
                    board[r][c] = 0
                elif board[r][c] == 3:
                    board[r][c] = 1
