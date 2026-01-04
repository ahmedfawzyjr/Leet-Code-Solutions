from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Solve a Sudoku puzzle using optimized backtracking with:
        1. Bitmasks for O(1) constraint checking
        2. MRV heuristic - fill cells with fewer options first
        """
        # Bitmasks: bit i represents digit (i+1)
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9
        
        # Initialize constraints from existing numbers
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = int(board[i][j]) - 1
                    mask = 1 << num
                    rows[i] |= mask
                    cols[j] |= mask
                    boxes[(i // 3) * 3 + j // 3] |= mask
        
        def get_candidates(i: int, j: int) -> int:
            """Get available numbers as bitmask."""
            return ~(rows[i] | cols[j] | boxes[(i // 3) * 3 + j // 3]) & 0x1FF
        
        def count_bits(x: int) -> int:
            """Count number of set bits."""
            count = 0
            while x:
                count += 1
                x &= x - 1
            return count
        
        def find_best_cell():
            """Find empty cell with minimum remaining values (MRV heuristic)."""
            min_count = 10
            best = None
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        candidates = get_candidates(i, j)
                        count = count_bits(candidates)
                        if count == 0:
                            return (-1, -1, 0)  # No valid options, need backtrack
                        if count < min_count:
                            min_count = count
                            best = (i, j, candidates)
                            if count == 1:
                                return best  # Can't do better
            return best
        
        def solve() -> bool:
            cell = find_best_cell()
            if cell is None:
                return True  # All cells filled
            
            i, j, candidates = cell
            if i == -1:
                return False  # Dead end
            
            box_idx = (i // 3) * 3 + j // 3
            
            # Try each candidate
            while candidates:
                # Get lowest set bit (next candidate)
                num = candidates & (-candidates)
                candidates &= candidates - 1
                
                # Place the number
                board[i][j] = str((num.bit_length()))
                rows[i] |= num
                cols[j] |= num
                boxes[box_idx] |= num
                
                if solve():
                    return True
                
                # Backtrack
                board[i][j] = '.'
                rows[i] &= ~num
                cols[j] &= ~num
                boxes[box_idx] &= ~num
            
            return False
        
        solve()
