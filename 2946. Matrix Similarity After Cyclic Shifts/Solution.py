from typing import List

class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        """
        You are given an m x n integer matrix mat and an integer k.
        The matrix rows are 0-indexed.
        Even-indexed rows (0, 2, 4, ..) are cyclically shifted to the left k times.
        Odd-indexed rows (1, 3, 5, ..) are cyclically shifted to the right k times.
        Return true if the final modified matrix after k steps is identical to the original matrix, 
        and false otherwise.
        """
        m = len(mat)
        n = len(mat[0])
        
        # A row remains the same after k cyclic shifts (left or right)
        # if and only if mat[i][j] == mat[i][(j + k) % n] for all j.
        for i in range(m):
            for j in range(n):
                if mat[i][j] != mat[i][(j + k) % n]:
                    return False
        return True
