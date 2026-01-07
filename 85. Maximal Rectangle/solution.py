from typing import List

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        
        rows = len(matrix)
        cols = len(matrix[0])
        heights = [0] * (cols + 1)
        max_area = 0
        
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0
            
            stack = [-1]
            for j in range(cols + 1):
                while heights[j] < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    w = j - stack[-1] - 1
                    max_area = max(max_area, h * w)
                stack.append(j)
                
        return max_area

if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    matrix1 = [
        ["1","0","1","0","0"],
        ["1","0","1","1","1"],
        ["1","1","1","1","1"],
        ["1","0","0","1","0"]
    ]
    print(f"Input: matrix = {matrix1}")
    print(f"Output: {sol.maximalRectangle(matrix1)}")
    
    # Example 2
    matrix2 = [["0"]]
    print(f"Input: matrix = {matrix2}")
    print(f"Output: {sol.maximalRectangle(matrix2)}")
    
    # Example 3
    matrix3 = [["1"]]
    print(f"Input: matrix = {matrix3}")
    print(f"Output: {sol.maximalRectangle(matrix3)}")
