from typing import List

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            return
        self.m, self.n = len(matrix), len(matrix[0])
        self.matrix = [[0] * self.n for _ in range(self.m)]
        self.bit = [[0] * (self.n + 1) for _ in range(self.m + 1)]
        for r in range(self.m):
            for c in range(self.n):
                self.update(r, c, matrix[r][c])

    def update(self, row: int, col: int, val: int) -> None:
        diff = val - self.matrix[row][col]
        self.matrix[row][col] = val
        i = row + 1
        while i <= self.m:
            j = col + 1
            while j <= self.n:
                self.bit[i][j] += diff
                j += j & (-j)
            i += i & (-i)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (self.query(row2 + 1, col2 + 1) - self.query(row1, col2 + 1) - 
                self.query(row2 + 1, col1) + self.query(row1, col1))

    def query(self, row: int, col: int) -> int:
        res = 0
        i = row
        while i > 0:
            j = col
            while j > 0:
                res += self.bit[i][j]
                j -= j & (-j)
            i -= i & (-i)
        return res

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)
