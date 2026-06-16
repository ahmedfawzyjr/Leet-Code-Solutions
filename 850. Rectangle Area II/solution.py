
from typing import List

class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        MOD = 10**9 + 7
        
        # Collect all unique x coordinates
        x_coords = set()
        for rect in rectangles:
            x_coords.add(rect[0])
            x_coords.add(rect[2])
        x_list = sorted(x_coords)
        
        total_area = 0
        
        # Iterate over consecutive x pairs
        for i in range(len(x_list) - 1):
            x1 = x_list[i]
            x2 = x_list[i + 1]
            dx = x2 - x1
            if dx == 0:
                continue
            
            # Collect all active y intervals for this x range
            y_intervals = []
            for rect in rectangles:
                if rect[0] <= x1 and rect[2] >= x2:
                    y_intervals.append((rect[1], rect[3]))
            
            if not y_intervals:
                continue
            
            # Merge y intervals
            y_intervals.sort()
            merged = []
            for y in y_intervals:
                if not merged:
                    merged.append(y)
                else:
                    last_y1, last_y2 = merged[-1]
                    curr_y1, curr_y2 = y
                    if curr_y1 <= last_y2:
                        # Overlapping, merge them
                        merged[-1] = (last_y1, max(last_y2, curr_y2))
                    else:
                        merged.append(y)
            
            # Calculate total y length
            y_length = 0
            for y1, y2 in merged:
                y_length += y2 - y1
            
            total_area += dx * y_length
        
        return total_area % MOD
