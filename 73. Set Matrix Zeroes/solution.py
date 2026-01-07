class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        
        O(1) space solution using first row and first column as markers.
        
        Time: O(m * n)
        Space: O(1)
        """
        if not matrix or not matrix[0]:
            return
        
        m, n = len(matrix), len(matrix[0])
        
        # Check if first row and first column need to be zeroed
        first_row_has_zero = any(matrix[0][j] == 0 for j in range(n))
        first_col_has_zero = any(matrix[i][0] == 0 for i in range(m))
        
        # Use first row and column as markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0  # Mark row
                    matrix[0][j] = 0  # Mark column
        
        # Zero out cells based on markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        # Zero out first row if needed
        if first_row_has_zero:
            for j in range(n):
                matrix[0][j] = 0
        
        # Zero out first column if needed
        if first_col_has_zero:
            for i in range(m):
                matrix[i][0] = 0


# Test cases
if __name__ == "__main__":
    sol = Solution()
    
    # Test case 1
    matrix1 = [[1,1,1],[1,0,1],[1,1,1]]
    sol.setZeroes(matrix1)
    print(f"Test 1: {matrix1}")  # Expected: [[1,0,1],[0,0,0],[1,0,1]]
    
    # Test case 2
    matrix2 = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    sol.setZeroes(matrix2)
    print(f"Test 2: {matrix2}")  # Expected: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
