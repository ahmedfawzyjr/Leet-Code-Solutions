from typing import List

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        row_sum = [0] * m
        col_sum = [0] * n
        
        for r in range(m):
            for c in range(n):
                if mat[r][c] == 1:
                    row_sum[r] += 1
                    col_sum[c] += 1
        
        ans = 0
        for r in range(m):
            for c in range(n):
                if mat[r][c] == 1 and row_sum[r] == 1 and col_sum[c] == 1:
                    ans += 1
        return ans
