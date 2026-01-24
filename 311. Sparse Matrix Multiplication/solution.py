from typing import List

class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        m, k, n = len(mat1), len(mat1[0]), len(mat2[0])
        res = [[0] * n for _ in range(m)]
        
        # Pre-process mat1 to find non-zero elements
        sparse_mat1 = []
        for r in range(m):
            for c in range(k):
                if mat1[r][c] != 0:
                    sparse_mat1.append((r, c, mat1[r][c]))
                    
        # Pre-process mat2 to find non-zero elements
        sparse_mat2 = []
        for r in range(k):
            for c in range(n):
                if mat2[r][c] != 0:
                    sparse_mat2.append((r, c, mat2[r][c]))
                    
        # Multiply using sparse representation
        for r1, c1, v1 in sparse_mat1:
            for r2, c2, v2 in sparse_mat2:
                if c1 == r2:
                    res[r1][c2] += v1 * v2
                    
        return res
