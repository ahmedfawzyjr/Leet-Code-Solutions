from typing import List
import bisect

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes:
            return 0
        
        # Sort by width ascending, then by height descending
        # This ensures that for the same width, we only pick one envelope (the one with the largest height)
        # when finding the LIS of heights.
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        
        # Find the LIS of heights
        heights = [e[1] for e in envelopes]
        lis = []
        for h in heights:
            idx = bisect.bisect_left(lis, h)
            if idx == len(lis):
                lis.append(h)
            else:
                lis[idx] = h
        
        return len(lis)
