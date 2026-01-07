class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        """
        Treat the 2D matrix as a 1D sorted array and perform binary search.
        
        Since each row is sorted and first element of each row > last element
        of previous row, we can treat it as a single sorted array.
        
        Index mapping: 
        - 1D index i → matrix[i // n][i % n] where n = number of columns
        
        Time: O(log(m * n))
        Space: O(1)
        """
        if not matrix or not matrix[0]:
            return False
        
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1
        
        while left <= right:
            mid = (left + right) // 2
            # Convert 1D index to 2D coordinates
            row, col = mid // n, mid % n
            mid_value = matrix[row][col]
            
            if mid_value == target:
                return True
            elif mid_value < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False
    
    def searchMatrix_two_binary_searches(self, matrix: list[list[int]], target: int) -> bool:
        """
        Alternative: Two binary searches - first find the row, then search within row.
        
        Time: O(log m + log n) = O(log(m * n))
        Space: O(1)
        """
        if not matrix or not matrix[0]:
            return False
        
        m, n = len(matrix), len(matrix[0])
        
        # Binary search to find the correct row
        top, bottom = 0, m - 1
        while top <= bottom:
            mid_row = (top + bottom) // 2
            if target < matrix[mid_row][0]:
                bottom = mid_row - 1
            elif target > matrix[mid_row][n - 1]:
                top = mid_row + 1
            else:
                # Target might be in this row
                break
        
        if top > bottom:
            return False
        
        # Binary search within the row
        row = (top + bottom) // 2
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False


# Test cases
if __name__ == "__main__":
    sol = Solution()
    
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    
    # Test case 1
    print(f"Test 1: {sol.searchMatrix(matrix, 3)}")  # Expected: True
    
    # Test case 2
    print(f"Test 2: {sol.searchMatrix(matrix, 13)}")  # Expected: False
    
    # Test with alternative method
    print(f"Test 1 (alt): {sol.searchMatrix_two_binary_searches(matrix, 3)}")  # Expected: True
    print(f"Test 2 (alt): {sol.searchMatrix_two_binary_searches(matrix, 13)}")  # Expected: False
