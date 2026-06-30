import math
from typing import List

class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        pos_x, pos_y = location
        angles = []
        same_location_count = 0
        
        for x, y in points:
            if x == pos_x and y == pos_y:
                same_location_count += 1
            else:
                angles.append(math.degrees(math.atan2(y - pos_y, x - pos_x)))
                
        angles.sort()
        # Duplicate angles with +360 to handle circular wrap-around
        angles += [a + 360 for a in angles]
        
        max_visible = 0
        left = 0
        n = len(angles) // 2
        
        for right in range(len(angles)):
            while angles[right] - angles[left] > angle:
                left += 1
            max_visible = max(max_visible, right - left + 1)
            
        return min(max_visible, n) + same_location_count
