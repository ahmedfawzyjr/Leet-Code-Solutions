from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        """
        Finds the minimum number of arrows required to burst all balloons.
        
        Time complexity: O(n log n) due to sorting.
        Space complexity: O(1) or O(n) depending on the sorting implementation.
        """
        if not points:
            return 0
        
        # Sort by the end position of the balloons
        points.sort(key=lambda x: x[1])
        
        arrows = 1
        curr_end = points[0][1]
        
        for i in range(1, len(points)):
            # If the current balloon starts after the last arrow's range
            if points[i][0] > curr_end:
                arrows += 1
                curr_end = points[i][1]
                
        return arrows
