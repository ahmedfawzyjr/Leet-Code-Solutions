from typing import List

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        # Sort by start point ascending, then by end point descending
        intervals.sort(key=lambda x: (x[0], -x[1]))
        
        count = 0
        max_end = 0
        
        for _, end in intervals:
            if end <= max_end:
                count += 1
            else:
                max_end = end
                
        return len(intervals) - count
