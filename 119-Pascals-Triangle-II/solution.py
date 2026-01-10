from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # We can optimize to O(rowIndex) space.
        # Initialize the row with 1s.
        row = [1] * (rowIndex + 1)
        
        # Calculate each row based on the previous one in-place.
        # We iterate backwards to avoid overwriting values we need for the next calculation.
        # For row i, we update values from index j = i-1 down to 1.
        # row[j] = row[j] + row[j-1]
        
        for i in range(2, rowIndex + 1):
            for j in range(i - 1, 0, -1):
                row[j] += row[j - 1]
                
        return row

if __name__ == "__main__":
    solution = Solution()
    
    # Example 1
    rowIndex1 = 3
    expected1 = [1, 3, 3, 1]
    result1 = solution.getRow(rowIndex1)
    print(f"Test Case 1: Expected {expected1}, Got {result1}")
    assert result1 == expected1
    
    # Example 2
    rowIndex2 = 0
    expected2 = [1]
    result2 = solution.getRow(rowIndex2)
    print(f"Test Case 2: Expected {expected2}, Got {result2}")
    assert result2 == expected2
    
    # Example 3
    rowIndex3 = 1
    expected3 = [1, 1]
    result3 = solution.getRow(rowIndex3)
    print(f"Test Case 3: Expected {expected3}, Got {result3}")
    assert result3 == expected3
    
    print("All test cases passed!")
