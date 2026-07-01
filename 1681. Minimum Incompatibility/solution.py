from collections import Counter
from typing import List

class Solution:
    def minimumIncompatibility(self, nums: List[int], k: int) -> int:
        n = len(nums)
        sz = n // k
        
        # If any number appears more than k times, it's impossible to partition
        # because at least one subset of size sz would have to contain a duplicate.
        counts = Counter(nums)
        if any(c > k for c in counts.values()):
            return -1
            
        nums.sort()
        memo = {}
        
        def solve(mask):
            if mask == (1 << n) - 1:
                return 0
            if mask in memo:
                return memo[mask]
            
            # Find the first available (unset) index
            # This breaks symmetry by forcing the subset to include the first available element.
            i = 0
            while (mask >> i) & 1:
                i += 1
                
            res = float('inf')
            
            def backtrack(curr_idx, count, current_mask, min_val, max_val):
                nonlocal res
                if count == sz:
                    res = min(res, (max_val - min_val) + solve(current_mask))
                    return
                
                last_used = -1
                for j in range(curr_idx + 1, n):
                    if not (current_mask & (1 << j)) and nums[j] > max_val and nums[j] != last_used:
                        last_used = nums[j]
                        backtrack(j, count + 1, current_mask | (1 << j), min_val, nums[j])
                        
            backtrack(i, 1, mask | (1 << i), nums[i], nums[i])
            memo[mask] = res
            return res
            
        ans = solve(0)
        return ans if ans != float('inf') else -1
