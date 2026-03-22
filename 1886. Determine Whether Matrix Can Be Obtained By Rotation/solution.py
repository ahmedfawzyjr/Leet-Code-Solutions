from typing import List


class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        """
        Calculates if the matrix 'mat' can be equal to 'target' by rotating it 90 degrees increments.
        
        Strategy: Rotate 90 degrees up to 4 times and compare with target.
        - Rotation: Transpose + Reverse each row
        
        Time Complexity: O(n^2) - rotating the matrix (n x n) four times
        Space Complexity: O(1) - rotate the matrix in-place
        """
        def rotate(matrix: List[List[int]]) -> None:
            """Rotate 90 degrees clockwise in-place."""
            n = len(matrix)
            # Step 1: Transpose
            for i in range(n):
                for j in range(i + 1, n):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            # Step 2: Reverse each row
            for i in range(n):
                matrix[i].reverse()
        
        # Check 0, 90, 180, 270 degrees
        for _ in range(4):
            if mat == target:
                return True
            rotate(mat)
        
        return False


if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    mat1 = [[0, 1], [1, 0]]
    target1 = [[1, 0], [0, 1]]
    print(f"Example 1: {sol.findRotation(mat1, target1)}")  # True
    
    # Example 2
    mat2 = [[0, 1], [1, 1]]
    target2 = [[1, 0], [0, 1]]
    print(f"Example 2: {sol.findRotation(mat2, target2)}")  # False
    
    # Example 3
    mat3 = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
    target3 = [[1, 1, 1], [0, 1, 0], [0, 0, 0]]
    print(f"Example 3: {sol.findRotation(mat3, target3)}")  # True
