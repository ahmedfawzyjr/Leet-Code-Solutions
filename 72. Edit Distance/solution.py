class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        Dynamic Programming solution for Edit Distance (Levenshtein Distance).
        
        dp[i][j] = minimum operations to convert word1[0:i] to word2[0:j]
        
        Time: O(m * n)
        Space: O(m * n), can be optimized to O(n)
        """
        m, n = len(word1), len(word2)
        
        # Create DP table with dimensions (m+1) x (n+1)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Base cases: converting empty string to word2[0:j] requires j insertions
        for j in range(n + 1):
            dp[0][j] = j
        
        # Base cases: converting word1[0:i] to empty string requires i deletions
        for i in range(m + 1):
            dp[i][0] = i
        
        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    # Characters match, no operation needed
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    # Take minimum of three operations:
                    # 1. Replace: dp[i-1][j-1] + 1
                    # 2. Delete from word1: dp[i-1][j] + 1
                    # 3. Insert into word1: dp[i][j-1] + 1
                    dp[i][j] = 1 + min(
                        dp[i - 1][j - 1],  # Replace
                        dp[i - 1][j],       # Delete
                        dp[i][j - 1]        # Insert
                    )
        
        return dp[m][n]


# Test cases
if __name__ == "__main__":
    sol = Solution()
    
    # Test case 1
    print(f"Test 1: {sol.minDistance('horse', 'ros')}")  # Expected: 3
    
    # Test case 2
    print(f"Test 2: {sol.minDistance('intention', 'execution')}")  # Expected: 5
