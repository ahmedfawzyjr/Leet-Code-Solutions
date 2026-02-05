class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        # If total sum of numbers is less than desiredTotal, nobody can reach it
        if (1 + maxChoosableInteger) * maxChoosableInteger / 2 < desiredTotal:
            return False
        
        memo = {}
        
        def solve(used_mask, current_total):
            if used_mask in memo:
                return memo[used_mask]
            
            for i in range(maxChoosableInteger):
                # Try choosing i+1
                if not (used_mask & (1 << i)):
                    # If this move reaches desiredTotal OR the next player cannot win
                    if current_total + i + 1 >= desiredTotal or not solve(used_mask | (1 << i), current_total + i + 1):
                        memo[used_mask] = True
                        return True
            
            memo[used_mask] = False
            return False
        
        return solve(0, 0)
