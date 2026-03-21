class Solution:
    def reverseSubmatrix(self, grid: list[list[int]], x: int, y: int, k: int) -> list[list[int]]:
        # The submatrix starts at (x, y) and has size k.
        # We need to reverse the order of its rows vertically.
        # row indices: x to x + k - 1
        # column indices: y to y + k - 1
        
        for i in range(k // 2):
            row1 = x + i
            row2 = x + k - 1 - i
            for j in range(y, y + k):
                grid[row1][j], grid[row2][j] = grid[row2][j], grid[row1][j]
        
        return grid
