from typing import List

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        dp = [[float('inf')] * (n + 1) for _ in range(m + 1)]
        
        dp[m][n-1] = 1
        dp[m-1][n] = 1
        
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                min_health_needed = min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j]
                dp[i][j] = max(1, min_health_needed)
                
        return dp[0][0]

if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    dungeon1 = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
    print(f"Example 1 Output: {sol.calculateMinimumHP(dungeon1)}") # Expected: 7
    
    # Example 2
    dungeon2 = [[0]]
    print(f"Example 2 Output: {sol.calculateMinimumHP(dungeon2)}") # Expected: 1
