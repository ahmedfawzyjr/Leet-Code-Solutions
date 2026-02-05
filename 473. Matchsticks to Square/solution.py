from typing import List

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if not matchsticks:
            return False
        
        total_sum = sum(matchsticks)
        if total_sum % 4 != 0:
            return False
        
        target = total_sum // 4
        matchsticks.sort(reverse=True)
        
        if matchsticks[0] > target:
            return False
        
        sides = [0] * 4
        
        def backtrack(index):
            if index == len(matchsticks):
                return all(side == target for side in sides)
            
            for i in range(4):
                if sides[i] + matchsticks[index] <= target:
                    sides[i] += matchsticks[index]
                    if backtrack(index + 1):
                        return True
                    sides[i] -= matchsticks[index]
                
                # If this side is 0, trying next sides will be redundant
                if sides[i] == 0:
                    break
            
            return False
        
        return backtrack(0)
