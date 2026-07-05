from typing import List

class Solution:
    def maxHappyGroups(self, batchSize: int, groups: List[int]) -> int:
        # Count the remainders of groups modulo batchSize
        counts = [0] * batchSize
        for g in groups:
            counts[g % batchSize] += 1
        
        # Groups with remainder 0 are always happy
        ans = counts[0]
        
        # Greedily pair up groups with remainder r and batchSize - r
        # because each pair (r, batchSize - r) can contribute 1 happy group
        # (the first one served starts at 0 remainder, hence happy; the second starts at r, not happy)
        for i in range(1, (batchSize + 1) // 2):
            j = batchSize - i
            if i == j:
                pairs = counts[i] // 2
                ans += pairs
                counts[i] -= pairs * 2
            else:
                pairs = min(counts[i], counts[j])
                ans += pairs
                counts[i] -= pairs
                counts[j] -= pairs
        
        # Now we use memoization / DFS to find the maximum happy groups for the remaining elements.
        memo = {}
        
        def dfs(state_tuple, rem):
            if state_tuple in memo:
                return memo[state_tuple]
            
            # If all counts are 0, we can't get any more happy groups
            if sum(state_tuple) == 0:
                return 0
            
            max_happy = 0
            # Try to pick any group with count > 0
            for i in range(1, batchSize):
                if state_tuple[i - 1] > 0:
                    # If the current remainder is 0, this group gets fresh donuts (happy)
                    happy = 1 if rem == 0 else 0
                    
                    # Create the next state
                    next_state = list(state_tuple)
                    next_state[i - 1] -= 1
                    next_state_tuple = tuple(next_state)
                    
                    next_rem = (rem + i) % batchSize
                    
                    max_happy = max(max_happy, happy + dfs(next_state_tuple, next_rem))
            
            memo[state_tuple] = max_happy
            return max_happy
        
        initial_state = tuple(counts[1:])
        ans += dfs(initial_state, 0)
        return ans
