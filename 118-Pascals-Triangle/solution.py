from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        
        for i in range(numRows):
            # The first and last row elements are always 1.
            row = [None for _ in range(i + 1)]
            row[0], row[-1] = 1, 1
            
            # Each triangle element (other than the first and last of each row)
            # is equal to the sum of the elements above-and-to-the-left and
            # above-and-to-the-right.
            for j in range(1, len(row) - 1):
                row[j] = triangle[i-1][j-1] + triangle[i-1][j]
            
            triangle.append(row)
            
        return triangle

if __name__ == "__main__":
    solution = Solution()
    
    # Example 1
    numRows1 = 5
    expected1 = [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
    result1 = solution.generate(numRows1)
    print(f"Test Case 1: Expected {expected1}, Got {result1}")
    assert result1 == expected1
    
    # Example 2
    numRows2 = 1
    expected2 = [[1]]
    result2 = solution.generate(numRows2)
    print(f"Test Case 2: Expected {expected2}, Got {result2}")
    assert result2 == expected2
    
    print("All test cases passed!")
