class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        """
        Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix.
        This matrix has the following properties:
        - Integers in each row are sorted in ascending from left to right.
        - Integers in each column are sorted in ascending from top to bottom.
        """
        if not matrix or not matrix[0]:
            return False
        
        m, n = len(matrix), len(matrix[0])
        row, col = 0, n - 1
        
        while row < m and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col -= 1
            else:
                row += 1
                
        return False

if __name__ == "__main__":
    sol = Solution()
    
    # Test Case 1
    matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
    target = 5
    result = sol.searchMatrix(matrix, target)
    print(f"Target: {target}, Found: {result} (Expected: True)")
    
    # Test Case 2
    target = 20
    result = sol.searchMatrix(matrix, target)
    print(f"Target: {target}, Found: {result} (Expected: False)")
