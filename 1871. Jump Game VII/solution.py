class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        """
        Determines if the last index of a binary string can be reached starting from index 0.
        Uses Dynamic Programming optimized with a sliding window approach (pre-sum of reachable indices).
        
        Complexity:
        - Time: O(N) where N is the length of the string s.
        - Space: O(N) to store the reachability status of each index.
        """
        n = len(s)
        if s[n - 1] == '1':
            return False
            
        # dp[i] is True if index i is reachable
        dp = [False] * n
        dp[0] = True
        
        # reachable_count keeps track of how many indices in the current 
        # jumping window [i - maxJump, i - minJump] are reachable.
        reachable_count = 0
        
        for i in range(1, n):
            # Add new index entering the window on the right side
            if i >= minJump:
                if dp[i - minJump]:
                    reachable_count += 1
            
            # Remove index leaving the window on the left side
            if i > maxJump:
                if dp[i - maxJump - 1]:
                    reachable_count -= 1
            
            # If current character is '0' and there's at least one reachable 
            # index in the window, then current index is reachable.
            if s[i] == '0' and reachable_count > 0:
                dp[i] = True
                
        return dp[n - 1]
