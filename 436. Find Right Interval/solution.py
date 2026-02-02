from typing import List
import bisect

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        # Store start times with their original indices
        starts = sorted([(interval[0], i) for i, interval in enumerate(intervals)])
        
        # Extract just the start times for binary search
        start_times = [s[0] for s in starts]
        
        res = []
        for interval in intervals:
            end = interval[1]
            # Use bisect_left to find the first start time >= end
            idx = bisect.bisect_left(start_times, end)
            
            if idx < len(start_times):
                res.append(starts[idx][1])
            else:
                res.append(-1)
                
        return res
