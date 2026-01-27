from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        m, n = len(matrix), len(matrix[0])
        memo = [[0] * n for _ in range(m)]
        
        def dfs(r, c):
            if memo[r][c] != 0:
                return memo[r][c]
            
            res = 1
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and matrix[nr][nc] > matrix[r][c]:
                    res = max(res, 1 + dfs(nr, nc))
            
            memo[r][c] = res
            return res
        
        ans = 0
        for i in range(m):
            for j in range(n):
                ans = max(ans, dfs(i, j))
        
        return ans

if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    matrix1 = [[9,9,4],[6,6,8],[2,1,1]]
    print(f"Example 1: {sol.longestIncreasingPath(matrix1)}") # Expected: 4
    
    # Example 2
    matrix2 = [[3,4,5],[3,2,6],[2,2,1]]
    print(f"Example 2: {sol.longestIncreasingPath(matrix2)}") # Expected: 4
    
    # Example 3
    matrix3 = [[1]]
    print(f"Example 3: {sol.longestIncreasingPath(matrix3)}") # Expected: 1
