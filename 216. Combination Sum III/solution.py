from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        """
        Find all valid combinations of k numbers that sum up to n such that the following conditions are true:
        - Only numbers 1 through 9 are used.
        - Each number is used at most once.
        
        Return a list of all possible valid combinations.
        
        We can use backtracking to explore all possible combinations.
        """
        result = []
        
        def backtrack(start_num, current_combination, current_sum):
            if len(current_combination) == k:
                if current_sum == n:
                    result.append(list(current_combination))
                return
            
            if current_sum > n:
                return
            
            for i in range(start_num, 10):
                # Optimization: if adding i exceeds n, no need to continue since i increases
                if current_sum + i > n:
                    break
                    
                current_combination.append(i)
                backtrack(i + 1, current_combination, current_sum + i)
                current_combination.pop()
                
        backtrack(1, [], 0)
        return result
