class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        one_step_before = 2
        two_steps_before = 1
        all_ways = 0
        
        for i in range(2, n):
            all_ways = one_step_before + two_steps_before
            two_steps_before = one_step_before
            one_step_before = all_ways
            
        return all_ways
