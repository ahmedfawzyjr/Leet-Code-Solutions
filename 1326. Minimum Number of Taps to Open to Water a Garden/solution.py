from typing import List

class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        # max_reach[i] will store the furthest index we can water starting from index i
        max_reach = [0] * (n + 1)
        for i, r in enumerate(ranges):
            left = max(0, i - r)
            right = min(n, i + r)
            max_reach[left] = max(max_reach[left], right)
        
        taps = 0
        curr_end = 0
        max_end = 0
        
        for i in range(n):
            max_end = max(max_end, max_reach[i])
            # If we cannot move forward past the current index i
            if max_end <= i:
                return -1
            
            # If we have reached the end of the current tap's coverage,
            # we must open another tap.
            if i == curr_end:
                taps += 1
                curr_end = max_end
                if curr_end >= n:
                    break
                    
        return taps if curr_end >= n else -1
