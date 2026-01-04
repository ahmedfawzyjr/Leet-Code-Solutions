from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Rotate the image by 90 degrees clockwise in-place.
        
        Strategy: Transpose + Reverse each row
        - Transpose: swap matrix[i][j] with matrix[j][i]
        - Reverse: reverse each row
        
        Time Complexity: O(n^2)
        Space Complexity: O(1)
        """
        n = len(matrix)
        
        # Step 1: Transpose the matrix (swap rows and columns)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # Step 2: Reverse each row
        for i in range(n):
            matrix[i].reverse()
    
    def rotate_layer_by_layer(self, matrix: List[List[int]]) -> None:
        """
        Alternative: Rotate layer by layer, four cells at a time.
        
        Time Complexity: O(n^2)
        Space Complexity: O(1)
        """
        n = len(matrix)
        
        for layer in range(n // 2):
            first = layer
            last = n - 1 - layer
            
            for i in range(first, last):
                offset = i - first
                
                # Save top
                top = matrix[first][i]
                
                # Left -> Top
                matrix[first][i] = matrix[last - offset][first]
                
                # Bottom -> Left
                matrix[last - offset][first] = matrix[last][last - offset]
                
                # Right -> Bottom
                matrix[last][last - offset] = matrix[i][last]
                
                # Top -> Right
                matrix[i][last] = top


# Test cases
if __name__ == "__main__":
    sol = Solution()
    
    # Example 1: 3x3 matrix
    matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    sol.rotate(matrix1)
    print(matrix1)  # [[7,4,1],[8,5,2],[9,6,3]]
    
    # Example 2: 4x4 matrix
    matrix2 = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    sol.rotate(matrix2)
    print(matrix2)  # [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
