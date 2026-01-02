from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        Generate all combinations of well-formed parentheses.
        
        Uses backtracking to build valid combinations by tracking
        the count of open and close parentheses.
        
        Time Complexity: O(4^n / sqrt(n)) - Catalan number
        Space Complexity: O(n) for recursion stack
        """
        result = []
        
        def backtrack(current: str, open_count: int, close_count: int):
            # Base case: if we've used all parentheses
            if len(current) == 2 * n:
                result.append(current)
                return
            
            # We can add '(' if we haven't used all of them
            if open_count < n:
                backtrack(current + '(', open_count + 1, close_count)
            
            # We can add ')' only if it doesn't exceed open count
            if close_count < open_count:
                backtrack(current + ')', open_count, close_count + 1)
        
        backtrack('', 0, 0)
        return result
