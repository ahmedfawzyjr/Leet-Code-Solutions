from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        # Sort by end time
        intervals.sort(key=lambda x: x[1])
        
        count = 0
        prev_end = intervals[0][1]
        
        for i in range(1, len(intervals)):
            if intervals[i][0] < prev_end:
                # Overlap, increment removal count
                count += 1
            else:
                # No overlap, update end time
                prev_end = intervals[i][1]
                
        return count
