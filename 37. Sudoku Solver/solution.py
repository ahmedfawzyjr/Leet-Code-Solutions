from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Solve a Sudoku puzzle by filling the empty cells.
        Modifies board in-place.
        
        Uses backtracking with constraint checking to find the valid solution.
        
        Time Complexity: O(9^(empty cells)) worst case, but pruning makes it faster
        Space Complexity: O(81) for recursion stack in worst case
        """
        def is_valid(row: int, col: int, num: str) -> bool:
            """Check if placing num at (row, col) is valid."""
            # Check row
            if num in board[row]:
                return False
            
            # Check column
            for i in range(9):
                if board[i][col] == num:
                    return False
            
            # Check 3x3 box
            box_row, box_col = 3 * (row // 3), 3 * (col // 3)
            for i in range(box_row, box_row + 3):
                for j in range(box_col, box_col + 3):
                    if board[i][j] == num:
                        return False
            
            return True
        
        def solve() -> bool:
            """Recursively solve the Sudoku using backtracking."""
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        for num in '123456789':
                            if is_valid(i, j, num):
                                board[i][j] = num
                                
                                if solve():
                                    return True
                                
                                # Backtrack
                                board[i][j] = '.'
                        
                        return False  # No valid number found
            
            return True  # All cells filled
        
        solve()
