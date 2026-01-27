from typing import List
import bisect

class SummaryRanges:

    def __init__(self):
        # Store intervals as [start, end] sorted by start
        self.intervals = []

    def addNum(self, value: int) -> None:
        # Find the position where the new value would be inserted
        # We use bisect_left to find the first interval with start >= value
        idx = bisect.bisect_left(self.intervals, [value, value])
        
        # Check if value is already covered by the previous interval
        if idx > 0 and self.intervals[idx-1][1] >= value:
            return
        
        # Check if value can be merged with neighbors
        merge_prev = (idx > 0 and self.intervals[idx-1][1] + 1 == value)
        merge_next = (idx < len(self.intervals) and self.intervals[idx][0] == value + 1)
        
        if merge_prev and merge_next:
            # Merge both: [start_prev, end_prev] + value + [start_next, end_next]
            self.intervals[idx-1][1] = self.intervals[idx][1]
            self.intervals.pop(idx)
        elif merge_prev:
            # Merge with previous: [start_prev, end_prev] + value
            self.intervals[idx-1][1] = value
        elif merge_next:
            # Merge with next: value + [start_next, end_next]
            self.intervals[idx][0] = value
        else:
            # Create new disjoint interval
            self.intervals.insert(idx, [value, value])

    def getIntervals(self) -> List[List[int]]:
        return self.intervals
