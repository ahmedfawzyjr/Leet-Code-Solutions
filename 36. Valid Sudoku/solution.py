from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        Determine if a 9x9 Sudoku board is valid.
        
        Only the filled cells need to be validated:
        1. Each row must contain digits 1-9 without repetition.
        2. Each column must contain digits 1-9 without repetition.
        3. Each of the 9 3x3 sub-boxes must contain digits 1-9 without repetition.
        
        Time Complexity: O(81) = O(1) - fixed board size
        Space Complexity: O(81) = O(1) - fixed number of sets
        """
        # Use sets to track seen digits in rows, columns, and boxes
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                
                if num == '.':
                    continue
                
                # Calculate box index (0-8)
                box_idx = (i // 3) * 3 + (j // 3)
                
                # Check if number already exists in row, column, or box
                if num in rows[i] or num in cols[j] or num in boxes[box_idx]:
                    return False
                
                # Add number to respective sets
                rows[i].add(num)
                cols[j].add(num)
                boxes[box_idx].add(num)
        
        return True
