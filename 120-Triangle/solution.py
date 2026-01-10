from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # We can solve this using DP.
        # We can modify the triangle in-place to store the minimum path sum to reach each element.
        # Or we can use O(n) space where n is the number of rows (which is also the max width).
        # Let's use O(n) space.
        # dp[j] will store the minimum path sum to reach index j in the current row.
        
        # Actually, iterating from bottom to top is easier.
        # dp[j] = min(dp[j], dp[j+1]) + triangle[i][j]
        # The base case is the last row.
        
        n = len(triangle)
        dp = triangle[-1][:]
        
        for i in range(n - 2, -1, -1):
            for j in range(i + 1):
                dp[j] = min(dp[j], dp[j+1]) + triangle[i][j]
                
        return dp[0]

if __name__ == "__main__":
    solution = Solution()
    
    # Example 1
    triangle1 = [[2],[3,4],[6,5,7],[4,1,8,3]]
    expected1 = 11
    result1 = solution.minimumTotal(triangle1)
    print(f"Test Case 1: Expected {expected1}, Got {result1}")
    assert result1 == expected1
    
    # Example 2
    triangle2 = [[-10]]
    expected2 = -10
    result2 = solution.minimumTotal(triangle2)
    print(f"Test Case 2: Expected {expected2}, Got {result2}")
    assert result2 == expected2
    
    print("All test cases passed!")
