class Solution:
    def numTrees(self, n: int) -> int:
        """
        Given an integer n, return the number of structurally unique BST's (binary search trees) 
        which has exactly n nodes of unique values from 1 to n.
        
        This is the Catalan number problem!
        
        Approach: Dynamic Programming
        - dp[i] = number of unique BSTs with i nodes
        - For each root value j from 1 to i:
          - Left subtree has (j-1) nodes -> dp[j-1] ways
          - Right subtree has (i-j) nodes -> dp[i-j] ways
          - Total for root j: dp[j-1] * dp[i-j]
        - dp[i] = sum of all combinations
        
        Time: O(n^2), Space: O(n)
        """
        # dp[i] = number of unique BSTs with i nodes
        dp = [0] * (n + 1)
        
        # Base cases
        dp[0] = 1  # Empty tree (null) - 1 way
        dp[1] = 1  # Single node - 1 way
        
        # Fill dp table
        for nodes in range(2, n + 1):
            for root in range(1, nodes + 1):
                left_trees = dp[root - 1]      # nodes in left subtree: 0 to root-1
                right_trees = dp[nodes - root]  # nodes in right subtree: root+1 to nodes
                dp[nodes] += left_trees * right_trees
        
        return dp[n]


if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    n1 = 3
    print(f"Input: n = {n1}")
    print(f"Output: {sol.numTrees(n1)}")  # Expected: 5
    
    # Example 2
    n2 = 1
    print(f"\nInput: n = {n2}")
    print(f"Output: {sol.numTrees(n2)}")  # Expected: 1
    
    # Additional test
    n3 = 4
    print(f"\nInput: n = {n3}")
    print(f"Output: {sol.numTrees(n3)}")  # Expected: 14
